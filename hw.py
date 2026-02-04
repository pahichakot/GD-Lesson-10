import pgzrun

#Setup
WIDTH = 870
HEIGHT = 650

TITLE = "Quiz Master"

#Boxes on screen
marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
timer_box = Rect(0, 0, 150, 150)
skip_box = Rect(0, 0, 150, 330)

#Position boxes
marquee_box.move_ip(0,0)
question_box.move_ip(20, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
timer_box.move_ip(700, 100)
skip_box.move_ip(700, 270)

#Variables and lists
score = 0
time_left = 10
is_game_over = False

question_file_name = "questions2.txt"
marquee_message = ""

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0 #Total number of questions
question_index = 0 #Current question

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "pink")
    screen.draw.filled_rect(skip_box, "purple")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "green")

    #Texts
    marquee_message = "Welcome to the Quiz Master !"+f"Q: {question_index} out of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox("Skip", skip_box, color = "white")
    screen.draw.textbox(question[0].strip(), question_box, color = "white")
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color = "white")
        index = index + 1

#Move marquee
def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0).split("|")



read_question_file()
question = read_next_question()
#question = ["Question: What is the farthest planet from the Sun?", "Earth", "Mercury", "Neptune", "Uranus", "3"]
pgzrun.go()