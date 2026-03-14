import matplotlib.pyplot as plt

class plot:
    def __init__(self):
        self.window_size = 100
        self.pitch_values1 = [0.0]*self.window_size
        self.pitch_values2 = [0.0]*self.window_size
        self.roll_values1 = [0.0]*self.window_size
        self.roll_values2 = [0.0]*self.window_size
        self.data_count = 0

        plt.ion()
        self.fig, (self.ax1,self.ax2,self.ax3) = plt.subplots(3)
        self.line1, = self.ax1.plot(self.pitch_values1)
        self.line2, = self.ax1.plot(self.pitch_values2)
        self.ax1.set_ylim(-180, 180)
        self.ax1.set_xlim(0, self.window_size)

        self.line3, = self.ax2.plot(self.roll_values1)
        self.line4, = self.ax2.plot(self.roll_values2)
        self.ax2.set_ylim(-180, 180)
        self.ax2.set_xlim(0, self.window_size)

        plt.show(block=False)

    def update(self, pitch1, pitch2, roll1, roll2):

        self.pitch_values1[self.data_count] = pitch1
        self.pitch_values2[self.data_count] = pitch2

        self.roll_values1[self.data_count] = roll1
        self.roll_values2[self.data_count] = roll2

        self.line1.set_ydata(self.pitch_values1)
        self.line1.set_xdata(range(self.window_size))

        self.line2.set_ydata(self.pitch_values2)
        self.line2.set_xdata(range(self.window_size))

        self.line3.set_ydata(self.roll_values1)
        self.line3.set_xdata(range(self.window_size))

        self.line4.set_ydata(self.roll_values2)
        self.line4.set_xdata(range(self.window_size))

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        self.data_count = (self.data_count + 1) % self.window_size