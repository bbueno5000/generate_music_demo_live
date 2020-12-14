"""
DOCSTRING
"""
import deepmusic
import glob
import os
import subprocess

class Utils:
    """
    Some utilities functions, to easily manipulate large volume of downloaded files.
    Independent of the main program but useful to extract/create the dataset.
    """
    def convert_midi2mp3(self):
        """
        Convert all midi files of the given directory to mp3
        """
        input_dir = 'docs/midi/'
        output_dir = 'docs/mp3/'
        assert os.path.exists(input_dir)
        os.makedirs(output_dir, exist_ok=True)
        print('Converting:')
        i = 0
        for filename in glob.iglob(os.path.join(input_dir, '**/*.mid'), recursive=True):
            print(filename)
            in_name = filename
            out_name = os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + '.mp3')
            command = 'timidity {} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {}'.format(
                in_name, out_name)
            subprocess.call(command, shell=True)
            i += 1
        print('{} files converted.'.format(i))

    def extract_files(self):
        """
        Recursively extract all files from a given directory
        """
        input_dir = '../www.chopinmusic.net/'
        output_dir = 'chopin_clean/'
        os.makedirs(output_dir, exist_ok=True)
        print('Extracting:')
        i = 0
        for filename in glob.iglob(os.path.join(input_dir, '**/*.mid'), recursive=True):
            print(filename)
            os.rename(filename, os.path.join(output_dir, os.path.basename(filename)))
            i += 1
        print('{} files extracted.'.format(i))

    def rename_files(self):
        """
        Rename all files of the given directory following some rules
        """
        input_dir = 'chopin/'
        output_dir = 'chopin_clean/'
        assert os.path.exists(input_dir)
        os.makedirs(output_dir, exist_ok=True)
        list_files = [f for f in os.listdir(input_dir) if f.endswith('.mid')]
        print('Renaming {} files:'.format(len(list_files)))
        for prev_name in list_files:
            new_name = prev_name.replace('midi.asp?file=', '')
            new_name = new_name.replace('%2F', '_')
            print('{} -> {}'.format(prev_name, new_name))
            os.rename(os.path.join(input_dir, prev_name), os.path.join(output_dir, new_name))

if __name__ == '__main__':
    Utils.convert_midi2mp3()
    composer = deepmusic.Composer()
    composer.main()
