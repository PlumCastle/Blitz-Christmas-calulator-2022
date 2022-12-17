import streamlit as st
import math
import numpy as np

header = st.container()

with header:
	st.title("Blitz Christmas event calculator")
	st.subheader("This is a calculator for figuring out how many wins/games/minutes/hours you need to play to grind through various event stages.")

	bells = st.number_input("How many bells do you need?",step = 1)
	no_of_wins = math.ceil(bells / 2)
	wr = st.number_input("What is your average win rate?")
	time_per_game = st.number_input("What is your average length for a match (in minutes)?")
	if st.button("Calculate wins"):
		st.write(f"The total number of wins needed to obtain {bells} bells is {no_of_wins}.")
		st.write(f"Assuming  you started the event on the 16th of December, you would need to win {math.ceil(no_of_wins / 11)} games a day.")

	if st.button("Calculate Games"):
		if wr <= 0:
			st.write("Please enter your average win rate.")
		else:
			st.write(f"The total number of games you would need to play to obtain {bells} bells is about {math.ceil((no_of_wins / wr) * 100)}. (may vary)")
			st.write(f"Assuming  you started the event on the 16th of December, you would need to play about {math.ceil(math.ceil((no_of_wins / wr) * 100) / 11)} games a day. (may vary)")

	if st.button("Calculate Time"):
		if wr <= 0:
			st.write("Please enter your average win rate.")
		elif time_per_game <= 0:
			st.write("Please enter your average length for a match.")
		else:
			time_m = math.ceil((no_of_wins / wr) * 100) * time_per_game
			time_h = time_m / 60
			st.write(f"The total ammount of time you would have to spend to obtain {bells} bells is about {np.round(time_m)} minutes or {np.round(time_h)} hours. (may vary)")
			st.write(f"Assuming  you started the event on the 16th of December, you would need to play about {np.round((time_m / 11),1)} minutes or {np.round((time_h / 11),1)} hours a day. (may vary)")
