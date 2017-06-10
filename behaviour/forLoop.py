MAX_PLAY_YAW=120
MIN_PLAY_PITCH=0
MAX_PLAY_PITCH=70
diff_yaw = [i for i in range(-MAX_PLAY_YAW, MAX_PLAY_YAW, 15)]
diff_pitch = [i for i in range(MIN_PLAY_PITCH, MAX_PLAY_PITCH, 15)]
path = []
for i in range(len(diff_pitch)):
  tmp = [diff_pitch[i] for j in range(len(diff_yaw))]
  print(tmp)
  path += zip(diff_yaw, tmp)
print(path)
