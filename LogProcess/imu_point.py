import re
import numpy as np
import matplotlib.pyplot as plt
path = "/home/yyj/logRobot/serial.log"
log = open(path, "r")

l0_check = r"roll: (-*\d{0,8}\.*\d{0,8}e*-*\d{0,8}) pitch: (-*\d{0,8}\.*\d{0,8}e*-*\d{0,8}) yaw: (-*\d{0,8}\.*\d{0,8}e*-*\d{0,8})"
l0_data = np.array([], dtype=np.float64)
l0_cnt = 0

for line in log:
    m0 = re.search(l0_check, line)

    if m0:
        print(m0.group(0))
        if l0_data.size == 0:
            l0_data = np.array([float(m0.group(1)), float(m0.group(2)), float(m0.group(3))])
        else:
            l0_data = np.vstack((l0_data, np.array([float(m0.group(1)), float(m0.group(2)), float(m0.group(3))])))
    l0_cnt += 1
print(l0_cnt)
print("shape", l0_data.shape)

begin_idx = 2440
end_idx = 5040
l0_data = np.delete(l0_data, slice(end_idx, l0_data.shape[0]), axis=0)
l0_data = np.delete(l0_data, slice(0, begin_idx), axis=0)

# print(l1_cnt)
# print(l2_cnt)
# print(l3_cnt)
# print(l4_cnt)
# print(l5_cnt)
log.close()
# begin_idx = 2200
# end_idx = 2850
# l0_data = np.delete(l0_data, slice(end_idx, l0_data.shape[0]), axis=0)
# l0_data = np.delete(l0_data, slice(0, begin_idx), axis=0)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l0_data[:, 0])
plt.plot(l0_data[:, 1])
plt.plot(l0_data[:, 2])
plt.ylabel('rpy')



plt.show()
np.savetxt("/home/yyj/logRobot/01151415_imu.csv", l0_data, delimiter=",")
