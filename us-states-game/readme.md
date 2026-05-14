# 🇺🇸 U.S. States Game (Python Turtle)

An interactive Python game built using the **Turtle graphics library** and **Pandas**, where players guess the names of U.S. states and see them appear on a map in real time.

This project focuses on **game logic, data handling with CSV files, and user interaction**, making it a great beginner-to-intermediate Python project.

---

## 🎮 How the Game Works

* A blank map of the United States is displayed.
* The player is prompted to enter U.S. state names.
* If the guessed state is correct:

  * The state name is displayed at its correct position on the map.
  * The score increases.
* The game continues until:

  * All 50 states are guessed, or
  * The user types **`Exit`**, or
  * The user clicks **Cancel**.

---

## 🛠️ Technologies Used

* **Python**
* **Turtle** – for graphics and UI
* **Pandas** – for reading and managing CSV data

---

## 📁 Project Structure

```
U.S-States-Game/
│
├── main.py                 # Main game logic
├── 50_states.csv           # State names with x, y coordinates
├── blank_states_img.gif    # U.S. map image
├── README.md               # Project documentation
```

---

## 📄 CSV File Format (`50_states.csv`)

The CSV file contains the state names along with their map coordinates:

```
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
...
```

These coordinates are used to place the state names accurately on the map.

---

## ▶️ How to Run the Game

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/U.S-States-Game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd U.S-States-Game
   ```

3. Make sure Python is installed (Python 3 recommended).

4. Install Pandas if not already installed:

   ```bash
   pip install pandas
   ```

5. Run the game:

   ```bash
   python main.py
   ```

---

## 🧠 Concepts Learned

* Turtle screen setup and image handling
* Working with Pandas DataFrames
* CSV file data manipulation
* Event-driven user input
* Game loops and condition handling
* Preventing duplicate guesses

---

## 🚀 Possible Improvements

* Save missing states to a CSV file when the game ends
* Add a timer or countdown mode
* Add sound effects
* Improve UI styling (fonts, colors)
* Convert the game into a class-based structure

---

## 📌 Why This Project?

This project is inspired by classic learning games and helps reinforce:

* Python fundamentals
* Data handling with real-world datasets
* Building interactive applications

---

## 🧑‍💻 Author

**Upendra Uddagiri**

Just tell me 💪😊
