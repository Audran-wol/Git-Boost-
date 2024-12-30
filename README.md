# 🚀 GitBoost - Supercharge Your GitHub Activity

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Website](https://img.shields.io/badge/website-gitboost.org-green.svg)](https://gitboost.org)
[![GitHub](https://img.shields.io/badge/github-Audran--wol-orange.svg)](https://github.com/Audran-wol)

GitBoost is a powerful tool that helps you maintain an active GitHub profile by creating customized commit patterns. Whether you're recovering lost commit history or ensuring consistent activity, GitBoost has got you covered! 

## ✨ Features

- 🎯 Custom date range selection
- 📊 Flexible commit frequency
- 🔄 Progress tracking with beautiful UI
- 🎨 Colorful command-line interface
- ⚡ Fast and efficient processing
- 🔒 Secure and clean operation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git installed and configured
- SSH access to GitHub

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Audran-wol/gitboost.git
cd gitboost
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 💫 Usage

1. Create a new repository on GitHub (DO NOT initialize it with README, license, or .gitignore)

2. Get your repository's SSH URL:
   - Go to your new repository
   - Click the "Code" button
   - Select "SSH"
   - Copy the URL (format: git@github.com:username/repo.git)

3. Run GitBoost:
```bash
python main.py
```

4. Follow the interactive prompts:
   - Enter your repository's SSH URL
   - Specify start date (YYYY-MM-DD)
   - Specify end date (YYYY-MM-DD)
   - Choose commits per day (1-10)

5. Watch the magic happen! 🎉

## ⚙️ Configuration

GitBoost will ask for:
- Repository SSH URL
- Start Date: When you want to begin commits (format: YYYY-MM-DD)
- End Date: When you want to end commits (format: YYYY-MM-DD)
- Commit Frequency: Number of commits per day (1-10)

## 🔒 Security

GitBoost operates in a temporary directory and only pushes commit history, ensuring your existing repository contents remain unchanged. We use SSH for secure GitHub authentication.

## 🤝 Support

- Website: [gitboost.org](https://gitboost.org)
- Email: info@gitboost.org
- GitHub: [@Audran-wol](https://github.com/Audran-wol)

## 💝 Support the Developer

If you find GitBoost helpful, consider supporting the developer:
- [Buy me a coffee](https://skrill.me/rq/Tiedang%20Yematha/5.00/EUR?key=E6Mu-Z-pyjnRej923zl53Rohtzt)

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🌟 Credits

Created with ❤️ by [Audran-wol](https://github.com/Audran-wol)

# 🚀 GitBoost - Supercharge Your GitHub Activity

[![GitHub](https://img.shields.io/badge/github-Audran--wol-orange.svg)](https://github.com/Audran-wol)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Audran%20Wolfhards-blue.svg)](https://www.linkedin.com/in/audran-wolfhards-7aab3321b/)
[![Instagram](https://img.shields.io/badge/Instagram-audran__germany-purple.svg)](https://www.instagram.com/audran_germany)

GitBoost is a powerful tool that helps you maintain an active GitHub profile by creating customized commit patterns. Whether you're recovering lost commit history or ensuring consistent activity, GitBoost has got you covered! 

## ✨ Features

- 🎯 Custom date range selection
- 📊 Flexible commit frequency (1-10 commits per day)
- 🔄 Real-time progress tracking
- 🎨 Beautiful command-line interface
- ⚡ Fast and efficient processing
- 🔒 Secure and clean operation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git installed and configured
- SSH key set up with GitHub

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Audran-wol/gitboost.git
cd gitboost
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Run the script:
```bash
python main.py
```

2. Follow the prompts:
   - Enter your repository SSH URL (e.g., git@github.com:username/repo.git)
   - Enter your GitHub email (same as in GitHub settings)
   - Select date range for commits
   - Choose commits per day (1-10)

3. Wait for the process to complete and check your GitHub profile!

## 🔧 Troubleshooting

1. SSH Key Issues:
   - Make sure you have an SSH key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
   - Add it to GitHub: Settings → SSH and GPG keys → New SSH key

2. Git Configuration:
   - Set your email: `git config --global user.email "your_email@example.com"`
   - Set your name: `git config --global user.name "Your Name"`

3. Repository Access:
   - Ensure you have write access to the repository
   - Check that your SSH key is properly set up

## 💝 Support the Project

If you find GitBoost helpful, consider supporting the development:

- [Buy me a coffee](https://skrill.me/rq/Tiedang%20Yematha/5/EUR?key=E6Mu-Z-pyjnRej923zl53Rohtzt)
- Star the repository
- Share with friends

## 📞 Connect with Me

- GitHub: [@Audran-wol](https://github.com/Audran-wol)
- LinkedIn: [Audran Wolfhards](https://www.linkedin.com/in/audran-wolfhards-7aab3321b/)
- Instagram: [@audran_germany](https://www.instagram.com/audran_germany)

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---
Made with ❤️ by Audran Wolfhards
