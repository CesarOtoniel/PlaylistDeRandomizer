import os
import random
import mutagen

def getMp3Duration(filePath):
    """Get the duration of an mp3 file in milliseconds."""
    audio = mutagen.File(filePath)
    return int(audio.info.length * 1000)

def replaceLineInLst(inputLst, outputLst, directory):
    # Read the list of mp3 files in the directory
    mp3Files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]
    
    if not mp3Files:
        print("No mp3 files found in the specified directory.")
        return

    # Read the input .lst file
    with open(inputLst, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Prepare the output content
    outputLines = []
    for line in lines:
        if "-1\t<placeholder_directory_path>" in line:  # Replace with the actual line to match
            if not mp3Files:
                print("No more unique mp3 files left to use.")
                break
            # Pick a random mp3 file and remove it from the list
            randomMp3 = random.choice(mp3Files)
            mp3Files.remove(randomMp3)
            # Get the duration of the mp3 file in milliseconds
            duration = getMp3Duration(randomMp3)
            # Replace the line with the new content
            newLine = f"{duration}\t{randomMp3}\n"
            outputLines.append(newLine)
        else:
            outputLines.append(line)

    # Write the output to a new .lst file with utf-8 encoding
    with open(outputLst, 'w', encoding='utf-8') as file:
        file.writelines(outputLines)

    print(f"Processed file saved as {outputLst}")

# Example usage:
inputLst = 'input.lst'  # Replace with the path to your input .lst file
outputLst = 'output.lst'  # Replace with the desired path for the output .lst file
directory = 'C:\\path\\to\\your\\directory'  # Replace with the path to your directory containing mp3 files
replaceLineInLst(inputLst, outputLst, directory)
