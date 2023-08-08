# This script creates a GUI for selecting two files: the source file containing
# the chapters of the video and the destination file containing the
# processed chapters

import PySimpleGUI as psg

from chapter_formatter import process_file, open_file


def create_layout() -> list:
    """Create a list of UI components"""
    layout = [
        [psg.Text("Select a source file:")],
        [psg.Input(size=(50, 10), disabled=True,
                   enable_events=True, key='-SOURCE-'),
         psg.FileBrowse(file_types=(("Text Files", "*.txt"),))
         ],
        [psg.Text("Select a destination file:")],
        [psg.Input(size=(50, 10), disabled=True,
                   key='-DESTINATION-', enable_events=True),
         psg.FileBrowse(file_types=(("Text Files", "*.txt"),))],
        [psg.Button("Process", key='-SUBMIT-'), psg.Exit()],
        [psg.HorizontalSeparator()],
        [psg.Text("Output")],
        [psg.Multiline(size=(60, 10), key='-DISPLAY-')],
    ]

    return layout


def main():
    """This function creates the GUI and handles events"""

    psg.theme("DarkAmber")

    window = psg.Window("Format Youtube Video Chapters",
                        layout=create_layout())

    while True:
        event, values = window.read()
        # print(event, values)

        if event == psg.WIN_CLOSED or event == 'Exit':
            break

        elif event in ('-SOURCE-', '-DESTINATION-'):
            file = values[event]
            window['-DISPLAY-'].Update(open_file(file_name=file))

        elif event == '-SUBMIT-':
            file1 = values['-SOURCE-']
            file2 = values['-DESTINATION-']
            window['-DISPLAY-'].update(f"{file1}\n{file2}")
            message = process_file(file_path=file1, new_file_path=file2)

            if "Success" in message:
                psg.popup(message, title=window.Title, auto_close=True,
                          auto_close_duration=5)
                window['-DISPLAY-'].update(open_file(file_name=file2))

            elif "Error" in message:
                psg.popup_error(message, title=window.Title,
                                auto_close=True, auto_close_duration=10)
                window['-DISPLAY-'].update(open_file(file_name=file1))

    window.close()


if __name__ == "__main__":
    main()
