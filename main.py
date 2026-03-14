import imu
import complementary_filter
import plot

mpu = imu.imu()
graphs = plot.plot()
filter1 = complementary_filter.complementary_filter()
filter2 = complementary_filter.complementary_filter(0.95)

mpu.calibrate()
while 1:
    mpu.calculate()
    pitch1 = filter1.calculate_pitch(mpu.gyro_pitch, mpu.acc_pitch)
    pitch2 = filter2.calculate_pitch(mpu.gyro_pitch, mpu.acc_pitch)
    roll1 = filter1.calculate_roll(mpu.gyro_roll, mpu.acc_roll)
    roll2 = filter2.calculate_roll(mpu.gyro_roll, mpu.acc_roll)
    graphs.update(pitch1, pitch2, roll1, roll2)
