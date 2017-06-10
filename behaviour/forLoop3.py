MIN_PLAY_PITCH = 0
MAX_PLAY_PITCH = 70
MIN_PLAY_YAW = -120
MAX_PLAY_YAW = 120
PLAY_STEP = 15
diff_pitch = [i for i in range(MIN_PLAY_PITCH, MAX_PLAY_PITCH, PLAY_STEP)]
diff_yaw = [i for i in range(-MAX_PLAY_YAW, MAX_PLAY_YAW, PLAY_STEP)]
len_pitch = len(diff_pitch)
len_yaw = len(diff_yaw)
pitch_yaw = []
for i in range(len(diff_pitch)):
  for j in range(len(diff_yaw)):
    pitch_iter = diff_pitch[i]
    if i%2==0 :
      yaw_iter = diff_yaw[-j - 1]
    else:
      yaw_iter = diff_yaw[j]
    pitch_yaw.append((pitch_iter, yaw_iter))
print(pitch_yaw)
