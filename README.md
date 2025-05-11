# Audio to MP3 Converter

A simple utility script that converts audio files to MP3 format while preserving the original directory structure.

## Features

- Converts various audio formats to MP3
- Preserves directory structure from input to output
- Uses ffmpeg for high-quality conversion
- Simple to use with minimal setup

## Prerequisites

- Python 3.x
- ffmpeg must be installed and available in your PATH

### Installing ffmpeg

- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

## Usage

1. Place your audio files in the `in` directory (will be created in the same folder as the script)
2. Run the script:

```bash
python3 convert.py
```

3. Converted MP3 files will be available in the `out` directory

## Directory Structure

```
/
├── convert.py          # The conversion script
├── in/                 # Place your source audio files here
│   ├── file1.wav
│   ├── subfolder/
│   │   └── file2.flac
│   └── ...
└── out/                # Converted MP3 files appear here
    ├── file1.mp3
    ├── subfolder/
    │   └── file2.mp3
    └── ...
```

## How It Works

The script performs the following operations:

1. Creates the `out` directory if it doesn't exist
2. Replicates the directory structure from `in` to `out`
3. Converts each audio file to MP3 format using ffmpeg with the libmp3lame codec
4. Places the converted files in the corresponding locations in the `out` directory

## Notes

- The script uses a quality setting of 2 (high quality) for the MP3 conversion
- Files with the same name will be overwritten in the output directory
- `.DS_Store` files are automatically skipped

## Troubleshooting

If you encounter errors during conversion:

1. Ensure ffmpeg is correctly installed and in your PATH
2. Check that you have read/write permissions for the directories
3. Verify that your source audio files are valid and not corrupted
