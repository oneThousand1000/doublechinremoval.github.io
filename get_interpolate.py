# save gif frames to interpolate

import os
import cv2

def save_gif_frames_to_interpolate(gif_path, output_dir):
    gif = cv2.VideoCapture(gif_path)
    os.makedirs(output_dir, exist_ok=True)
    frame_idx = 0
    while True:
        ret, frame = gif.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(output_dir, f'{frame_idx:06d}.jpg'), frame)
        frame_idx += 1
    gif.release()


gif_path = "F:\sig2021\doublechinremoval.github.io\static\interpolation\stacked/1.gif"
output_dir = "F:\sig2021\doublechinremoval.github.io\static\interpolation\stacked"


save_gif_frames_to_interpolate(gif_path, output_dir)
