import streamlit as st
import time
import threading
from get_price import GetPrice
from alert_manager import Alerts

# --- Page Config ---
st.set_page_config(
    page_title="Price Tracker",
    page_icon="🎯",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.04em;
    background: linear-gradient(135deg, #f0f0ff 0%, #a78bfa 50%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.25rem;
}

.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #6b6b8a;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
}

.price-display {
    background: linear-gradient(135deg, #13131f 0%, #1a1a2e 100%);
    border: 1px solid #2a2a45;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
}

.price-display::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #a78bfa, #60a5fa, transparent);
}

.price-number {
    font-family: 'Space Mono', monospace;
    font-size: 3.5rem;
    font-weight: 700;
    color: #e8e8f0;
    line-height: 1;
}

.price-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #6b6b8a;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}

.status-below {
    background: linear-gradient(135deg, #0f2a1a, #0a3020);
    border: 1px solid #1a5c35;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #4ade80;
    margin: 1rem 0;
}

.status-above {
    background: linear-gradient(135deg, #2a1a0f, #301a0a);
    border: 1px solid #7c3a15;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #fb923c;
    margin: 1rem 0;
}

.monitor-card {
    background: #13131f;
    border: 1px solid #2a2a45;
    border-radius: 16px;
    padding: 1.75rem;
    margin: 1rem 0;
}

.monitor-header {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #6b6b8a;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.pulse-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #4ade80;
    box-shadow: 0 0 8px #4ade80;
    margin-right: 8px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

div[data-testid="stTextInput"] > div > div > input {
    background: #13131f !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    padding: 0.75rem 1rem !important;
}

div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 2px rgba(167,139,250,0.15) !important;
}

div[data-testid="stNumberInput"] > div > div > input {
    background: #13131f !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'Space Mono', monospace !important;
}

label[data-testid="stWidgetLabel"] > div > p {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
    color: #6b6b8a !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

div[data-testid="stSlider"] {
    padding: 0.5rem 0;
}

.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.65rem 1.5rem !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(124,58,237,0.4) !important;
}

div[data-testid="stSelectSlider"] {
    padding: 0.5rem 0;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e30;
    margin: 2rem 0;
}

.log-entry {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: #6b6b8a;
    padding: 0.35rem 0;
    border-bottom: 1px solid #1a1a2e;
}

.log-entry.success { color: #4ade80; }
.log-entry.warning { color: #fb923c; }
.log-entry.info { color: #60a5fa; }
</style>
""", unsafe_allow_html=True)


# --- Init session state ---
for key, default in {
    "current_price": None,
    "monitoring": False,
    "log": [],
    "check_count": 0,
    "alert_sent": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def add_log(msg, level="info"):
    ts = time.strftime("%H:%M:%S")
    st.session_state.log.insert(0, {"msg": msg, "level": level, "ts": ts})
    if len(st.session_state.log) > 30:
        st.session_state.log = st.session_state.log[:30]


# --- Header ---
st.markdown('<div class="hero-title">Price Tracker</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">// Amazon deal monitor & alert system</div>', unsafe_allow_html=True)

# --- Input Section ---
st.markdown('<div class="monitor-card"><div class="monitor-header">// Target Configuration</div>', unsafe_allow_html=True)

url = st.text_input("Product URL", placeholder="https://www.amazon.com/dp/...")
target_price = st.number_input("Target Price ($)", min_value=0.01, value=50.00, step=0.01, format="%.2f")

col1, col2 = st.columns(2)
with col1:
    check_now = st.button("⚡ Check Price Now")
with col2:
    interval_options = {"1 min": 60, "5 min": 300, "15 min": 900, "30 min": 1800, "1 hr": 3600}
    interval_label = st.selectbox("Monitor Interval", list(interval_options.keys()), index=1, label_visibility="visible")

st.markdown('</div>', unsafe_allow_html=True)

# --- Check Price Now ---
if check_now:
    if not url.strip():
        st.warning("Please enter a product URL.")
    else:
        with st.spinner("Fetching price..."):
            fetcher = GetPrice()
            price = fetcher.get_current_price(url.strip())
            st.session_state.current_price = price
            st.session_state.check_count += 1
            if price is not None:
                add_log(f"Price fetched: ${price:.2f}", "success")
                if price < target_price:
                    add_log(f"Price ${price:.2f} is BELOW target ${target_price:.2f} — sending alert!", "success")
                    try:
                        alerts = Alerts()
                        alerts.send_alert(url.strip())
                        st.session_state.alert_sent = True
                        add_log("Email alert sent successfully.", "success")
                    except Exception as e:
                        add_log(f"Alert failed: {e}", "warning")
                else:
                    add_log(f"Price ${price:.2f} above target ${target_price:.2f} — no alert.", "info")
            else:
                add_log("Failed to retrieve price. Check URL or connection.", "warning")

# --- Price Display ---
if st.session_state.current_price is not None:
    p = st.session_state.current_price
    st.markdown(f"""
    <div class="price-display">
        <div class="price-number">${p:,.2f}</div>
        <div class="price-label">Current Price</div>
    </div>
    """, unsafe_allow_html=True)

    if p < target_price:
        diff = target_price - p
        st.markdown(f"""
        <div class="status-below">
            ✓ &nbsp; ${p:.2f} is ${diff:.2f} below your target of ${target_price:.2f} — alert triggered!
        </div>
        """, unsafe_allow_html=True)
    else:
        diff = p - target_price
        st.markdown(f"""
        <div class="status-above">
            ↑ &nbsp; ${p:.2f} is ${diff:.2f} above your target of ${target_price:.2f}
        </div>
        """, unsafe_allow_html=True)

# --- Auto Monitor ---
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<div class="monitor-card"><div class="monitor-header">// Auto Monitor</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    start_monitor = st.button("▶ Start Monitoring")
with col4:
    stop_monitor = st.button("■ Stop Monitoring")

if start_monitor:
    if not url.strip():
        st.warning("Enter a URL first.")
    else:
        st.session_state.monitoring = True
        add_log(f"Monitoring started every {interval_label}.", "info")

if stop_monitor:
    st.session_state.monitoring = False
    add_log("Monitoring stopped.", "warning")

if st.session_state.monitoring:
    interval_seconds = interval_options[interval_label]
    st.markdown(f"""
    <div style="display:flex;align-items:center;font-family:'Space Mono',monospace;font-size:0.75rem;color:#4ade80;margin:0.5rem 0;">
        <span class="pulse-dot"></span> Monitoring active &mdash; checks every {interval_label}
    </div>
    """, unsafe_allow_html=True)

    # Run one live check per rerun cycle during monitoring
    if url.strip():
        fetcher = GetPrice()
        price = fetcher.get_current_price(url.strip())
        st.session_state.current_price = price
        st.session_state.check_count += 1
        if price is not None:
            add_log(f"Auto-check: ${price:.2f}", "info")
            if price < target_price and not st.session_state.alert_sent:
                try:
                    alerts = Alerts()
                    alerts.send_alert(url.strip())
                    st.session_state.alert_sent = True
                    add_log("Alert email sent!", "success")
                except Exception as e:
                    add_log(f"Alert failed: {e}", "warning")
        else:
            add_log("Auto-check failed to retrieve price.", "warning")

        time.sleep(interval_seconds)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- Stats Row ---
if st.session_state.check_count > 0:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Checks Run", st.session_state.check_count)
    with c2:
        st.metric("Target Price", f"${target_price:.2f}")
    with c3:
        st.metric("Alerts Sent", "Yes" if st.session_state.alert_sent else "No")

# --- Activity Log ---
if st.session_state.log:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="monitor-header" style="font-family:\'Space Mono\',monospace;font-size:0.65rem;color:#6b6b8a;letter-spacing:0.2em;text-transform:uppercase;">// Activity Log</div>', unsafe_allow_html=True)
    log_html = ""
    for entry in st.session_state.log[:10]:
        log_html += f'<div class="log-entry {entry["level"]}">[{entry["ts"]}] {entry["msg"]}</div>'
    st.markdown(log_html, unsafe_allow_html=True)
