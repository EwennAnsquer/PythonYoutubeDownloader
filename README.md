PythonYouTubeDownloader

PythonYouTubeDownloader is a console-based application that enables users to download YouTube videos directly to their local machines. This project leverages the pytube library, a lightweight Python library for downloading YouTube content.
Features

    Download Videos: Fetch and save YouTube videos in various resolutions and formats.
    Progress Tracking: Monitor download progress in real-time through console output.
    Error Handling: Gracefully manages exceptions and provides informative messages for common issues.

Prerequisites

    Python 3.x: Ensure that Python is installed on your system.

    pytube Library: This can be installed using pip.

    pip install pytube

Installation

    Clone the Repository:

git clone https://github.com/EwennAnsquer/PythonYouTubeDownloader.git
cd PythonYouTubeDownloader

Install Dependencies:

Install the required Python libraries:

    pip install -r requirements.txt

    Note: If requirements.txt is not provided, manually install pytube as shown above.

Usage

    Run the Application:

    Execute the Python script:

    python downloader.py

    Provide Video URL:

    When prompted, enter the URL of the YouTube video you wish to download.

    Select Stream:

    The application will display available streams. Choose the desired stream by entering the corresponding itag value.

    Download Video:

    The selected video will begin downloading to the specified directory.

Contributing

Contributions are welcome! To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -m 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Open a Pull Request detailing your changes.

License

This project is licensed under the MIT License. For more details, refer to the LICENSE file.
Acknowledgements

    pytube: The essential library powering this downloader.
    youtube-dl: An alternative tool for downloading YouTube videos.

Note: Downloading videos from YouTube may violate YouTube's Terms of Service. This tool is intended for personal use and educational purposes only. Ensure you have the necessary permissions before downloading and using content.
