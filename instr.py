from PyQt5.QtCore import QTime
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'welcome to the Health status detection program!'
txt_next = 'Start'
txt_instruction = (
    'This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
    'The Rufier test is a set of phhysical exercises designed to assess your cardiac perfomance during physical exertion.\n'
    'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
    'then, within 45 seconds, the subject perfoms 30 squats.\n'
    'when the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
    'and then for the last 15 seconds of the first minute of the recovery period.\n'
    'Important! If you feel unwell during the test (dizziness, \n'
    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.'
)  

txt_title = 'Health'
txt_name = 'Enter Your full name:'
txt_hintname = 'Full name'
txt_hintage = '0'
txt_test1 = (
    'Lie on your back and take your pulsefoor 15 seconds.'
    'Click the "Start first test" button to start the timer.\n'
    'Write down the result in the appropriate field.'
)

txt_test2 = (
    'Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button\n'
    'to start the squat counter.'
)

txt_test3 = (
    'Lie on your back and take your pulse for the first 15 seconds of the minute,'
    'then for the last 15 seconds of the minute. \n'
    'Press the "Start final test" button to start the timer.\n'
    'The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black.'
    'Write down the results in the appropriate fields.'
)

txt_sendresults = 'Send the results'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'

txt_starttest1 = 'Start the first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start the final test'
txt_timer = ''

txt_age = 'Full years'
txt_finalwin = 'Results'
txt_index = 'Roufier Index:'
txt_workheart = 'Cardiac perfomance'
txt_res1 = "low. See your doctor right away!"
txt_res2 = "satisfactory. See your doctor!"
txt_res3 = "average. It may be worth seeing your doctor to get checked out."
txt_res4 = "above avarage"
txt_res5 = "high"