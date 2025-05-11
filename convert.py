#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_directory_structure(input_dir, output_dir):
    """
    Create the same directory structure in output_dir as in input_dir
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        # Get the relative path from input_dir
        rel_path = os.path.relpath(root, input_dir)
        
        # Create corresponding directory in output_dir
        if rel_path != '.':
            target_dir = os.path.join(output_dir, rel_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

def convert_files_to_mp3(input_dir, output_dir):
    """
    Convert all audio files in input_dir to MP3 in output_dir
    """
    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        # Get the relative path from input_dir
        rel_path = os.path.relpath(root, input_dir)
        
        # Process each file
        for file in files:
            # Skip .DS_Store files
            if file == '.DS_Store':
                continue
                
            input_file = os.path.join(root, file)
            
            # Determine the output path and change the extension to .mp3
            if rel_path == '.':
                output_path = output_dir
            else:
                output_path = os.path.join(output_dir, rel_path)
            
            # Get file name without extension and add .mp3
            file_name = os.path.splitext(file)[0] + '.mp3'
            output_file = os.path.join(output_path, file_name)
            
            # Convert the file using ffmpeg
            try:
                subprocess.run([
                    'ffmpeg',
                    '-y',                # Overwrite output files
                    '-i', input_file,    # Input file
                    '-codec:a', 'libmp3lame',  # Audio codec
                    '-qscale:a', '2',     # Quality scale
                    output_file          # Output file
                ], check=True)
                print(f"Converted {input_file} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {input_file}: {e}", file=sys.stderr)
            except Exception as e:
                print(f"Unexpected error with {input_file}: {e}", file=sys.stderr)

def main():
    # Define input and output directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'in')
    output_dir = os.path.join(script_dir, 'out')
    
    # Create the output directory structure
    create_directory_structure(input_dir, output_dir)
    
    # Convert all files to MP3
    convert_files_to_mp3(input_dir, output_dir)
    
    print("Conversion completed.")

if __name__ == "__main__":
    main()