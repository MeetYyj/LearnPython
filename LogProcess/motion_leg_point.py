import re
import numpy as np
import matplotlib.pyplot as plt
path = "/home/yyj/logRobot/motion.log"
log = open(path, "r")
l0_check = r"l0 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l1_check = r"l1 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l2_check = r"l2 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l3_check = r"l3 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l4_check = r"l4 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l5_check = r"l5 f(\d+) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8}) (-*\d{0,8}\.*\d{0,8})"
l0_data = np.array([], dtype=np.float64)
l1_data = np.array([], dtype=np.float64)
l2_data = np.array([], dtype=np.float64)
l3_data = np.array([], dtype=np.float64)
l4_data = np.array([], dtype=np.float64)
l5_data = np.array([], dtype=np.float64)
l0_cnt = 0
l1_cnt = 0
l2_cnt = 0
l3_cnt = 0
l4_cnt = 0
l5_cnt = 0
for line in log:
    m0 = re.search(l0_check, line)
    m1 = re.search(l1_check, line)
    m2 = re.search(l2_check, line)
    m3 = re.search(l3_check, line)
    m4 = re.search(l4_check, line)
    m5 = re.search(l5_check, line)
    if m0:
        if l0_data.size == 0:
            l0_data = np.array([float(m0.group(2)), float(m0.group(3)), float(m0.group(4))])
        else:
            l0_data = np.vstack((l0_data, np.array([float(m0.group(2)), float(m0.group(3)), float(m0.group(4))])))
        l0_cnt += 1
    if m1:
        if l1_data.size == 0:
            l1_data = np.array([float(m1.group(2)), float(m1.group(3)), float(m1.group(4))])
        else:
            l1_data = np.vstack((l1_data, np.array([float(m1.group(2)), float(m1.group(3)), float(m1.group(4))])))
        l1_cnt += 1
    if m2:
        if l2_data.size == 0:
            l2_data = np.array([float(m2.group(2)), float(m2.group(3)), float(m2.group(4))])
        else:
            l2_data = np.vstack((l2_data, np.array([float(m2.group(2)), float(m2.group(3)), float(m2.group(4))])))
        l2_cnt += 1
    if m3:
        if l3_data.size == 0:
            l3_data = np.array([float(m3.group(2)), float(m3.group(3)), float(m3.group(4))])
        else:
            l3_data = np.vstack((l3_data, np.array([float(m3.group(2)), float(m3.group(3)), float(m3.group(4))])))
        l3_cnt += 1
    if m4:
        if l4_data.size == 0:
            l4_data = np.array([float(m4.group(2)), float(m4.group(3)), float(m4.group(4))])
        else:
            l4_data = np.vstack((l4_data, np.array([float(m4.group(2)), float(m4.group(3)), float(m4.group(4))])))
        l4_cnt += 1
    if m5:
        if l5_data.size == 0:
            l5_data = np.array([float(m5.group(2)), float(m5.group(3)), float(m5.group(4))])
        else:
            l5_data = np.vstack((l5_data, np.array([float(m5.group(2)), float(m5.group(3)), float(m5.group(4))])))
        l5_cnt += 1
print("shape", l0_data.shape)
print("shape", l1_data.shape)
print("shape", l2_data.shape)
print("shape", l3_data.shape)
print("shape", l4_data.shape)
print("shape", l5_data.shape)
begin_idx = 2200
end_idx = 2850
l0_data = np.delete(l0_data, slice(end_idx, l0_data.shape[0]), axis=0)
l0_data = np.delete(l0_data, slice(0, begin_idx), axis=0)
l1_data = np.delete(l1_data, slice(end_idx, l1_data.shape[0]), axis=0)
l1_data = np.delete(l1_data, slice(0, begin_idx), axis=0)
l2_data = np.delete(l2_data, slice(end_idx, l2_data.shape[0]), axis=0)
l2_data = np.delete(l2_data, slice(0, begin_idx), axis=0)
l3_data = np.delete(l3_data, slice(end_idx, l3_data.shape[0]), axis=0)
l3_data = np.delete(l3_data, slice(0, begin_idx), axis=0)
l4_data = np.delete(l4_data, slice(end_idx, l4_data.shape[0]), axis=0)
l4_data = np.delete(l4_data, slice(0, begin_idx), axis=0)
l5_data = np.delete(l5_data, slice(end_idx, l5_data.shape[0]), axis=0)
l5_data = np.delete(l5_data, slice(0, begin_idx), axis=0)
# print(l1_cnt)
# print(l2_cnt)
# print(l3_cnt)
# print(l4_cnt)
# print(l5_cnt)
log.close()
plt.subplot(6, 1, 1)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l0_data[:, 2])
plt.ylabel('leg_0 xyz')

plt.subplot(6, 1, 2)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l1_data[:, 2])
plt.ylabel('leg_1 xyz')

plt.subplot(6, 1, 3)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l2_data[:, 2])
plt.ylabel('leg_2 xyz')

plt.subplot(6, 1, 4)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l3_data[:, 2])
plt.ylabel('leg_3 xyz')

plt.subplot(6, 1, 5)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l4_data[:, 2])
plt.ylabel('leg_4 xyz')

plt.subplot(6, 1, 6)
# plt.figure(figsize=(30, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(l5_data[:, 2])
plt.ylabel('leg_5 xyz')
plt.show()

l_all_data = np.concatenate((l0_data, l1_data), axis=1)
l_all_data = np.concatenate((l_all_data, l2_data), axis=1)
l_all_data = np.concatenate((l_all_data, l3_data), axis=1)
l_all_data = np.concatenate((l_all_data, l4_data), axis=1)
l_all_data = np.concatenate((l_all_data, l5_data), axis=1)

np.savetxt("/home/yyj/logRobot/01142104f_l_all.csv", l_all_data, delimiter=",")


# plt.plot(l0_data[:, 2])
# plt.ylabel('leg_0 xyz')
plt.show()
