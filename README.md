# NUS HacknRoll-2024 (Top 8 Teams) - Sign Race

HacknRoll NUS Hackers 2024 Hackathon Competition

Inspiration
We are Typeracer lovers, but it got more boring, therefore, we integrated machine learning into the game by using sign language as a medium to type. This way, more physical interaction is involved and aims to make the game more interactive and lively, as well as provide a way for people to practice signing in a fun way. At the same time, we would like to delve into the advanced world of Machine Learning, particularly computer vision by the infamous OpenCV library, hence we believe this project will be a catalyst for us to do just that.

What it does
The game initially begins with a simple interface of the main menu, where a start button is ready to be clicked by player. When the button is clicked, a random keyword will shows up. The webcamera will turn on, and the player must fingerspell the keyword using the correct ASL alphabets. If the player succeeds, they will be taken back to the main menu where they can play again. The main menu also contains a leaderboard that shows the top fastest five players, with timing being calculated through the speed of their characters-per-second.

How we built it
It goes through four phases:

Sign language recognition
Racer game
Scoreboard
GUI
ASL alphabet recognition was conducted with the utilisation of OpenCV library by providing it with datasets of each sign, with us personally creating and training the model through providing our own personal raw data. Then, we created the typeracer game in which a keyword is randomised for the player to show the correct sign. The scoreboard was generated using a CSV file, where rankings for the top five players are recorded. Lastly, a GUI was created for the game interface.

Challenges we ran into
The most challenging aspect is merging all of the feature we have implemented. A few functions in the main file were not able to work properly due to new implementation. Nevertheless, we managed to do some trial and error to detect the fault. With this strategy, we were able to solve and merge all the feature into a single file. Furthermore, it was all of our first time working with this sort of Machine Learning and training our own models, so it was a challenge figuring out how to go about doing it. While we made some mistakes and ran into head-scratching problems along the way due to our inexperience, it was rewarding to grow and overcome those challenge, learning much more about Machine Learning through it. For example, our model was initially not very accurate due to only using around 40 raw data samples per class, which we eventually realised and overcame by providing up to around 300 more raw data samples per class.

Accomplishments that we're proud of
It was our first time to working with Machine Learning. We are proud of the fact that despite our inexperience and lack of knowledge, we could successfully build our typeracer.

What's next for Sign Racer
We aim to implement the game for different types of sign languages that utilise some form of alphabets, such as Japanese Sign Language, British Sign Language etc. Furthermore, we could expand on ASL and have our game test on signing actual ASL words instead of a single fingerspelled word, upgrading our model to account for gestures as well.

Built With
- opencv
- python
- teachablemachine
- tkinter
- visual-studio-code

https://devpost.com/software/the-furious-of-sign-racer
