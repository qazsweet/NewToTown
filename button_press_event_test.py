from matplotlib import pyplot as plt

class LineBuilder:
    def __init__(self, lineli):
        self.line = lineli
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = lineli.figure.canvas.mpl_connect('button_press_event', self)
        print(type(lineli))

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()
