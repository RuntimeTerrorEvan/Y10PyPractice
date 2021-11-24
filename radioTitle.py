import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

#plt.scatter(1, 2, color = 'yellow')

fig, ax = plt.subplots()
ax.set_title('yellow plot',
             fontsize=18)

rax = plt.axes([0.175, 0.6, 0.25, 0.25])
radio_button = RadioButtons(rax, ('yellow',
                                  'red',
                                  'blue',
                                  'green'))



def colorfunc(label):
    ax.set_title(label +  ' plot',  fontsize=18)
    plt.draw()
 
radio_button.on_clicked(colorfunc)                                 

plt.show()
