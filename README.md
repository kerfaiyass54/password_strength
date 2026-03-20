# Password Strength Analyzer 🔐✨

**A comprehensive password strength evaluation system combining machine learning and intuitive UI**

[![My Skills](https://skillicons.dev/icons?i=py,vscode,pycharm,fastapi,angular,html,css,ts,sklearn)](https://skillicons.dev)


---

## 🚀 Overview

**Password Strength Analyzer** is a sophisticated system that evaluates password strength using machine learning models and provides real-time feedback through an intuitive Angular interface. This project combines:

- **Machine Learning Model**: Trained on real password datasets to predict strength (weak/medium/strong)
- **Feature Engineering**: Extracts 7 key password characteristics for analysis
- **FastAPI Backend**: Efficient REST API for password evaluation
- **Angular Frontend**: Interactive UI with real-time feedback

Perfect for developers, security professionals, and anyone who needs to implement robust password validation systems.

---

## ✨ Features

✅ **Machine Learning Powered**: Uses Random Forest classifier trained on real password data

✅ **Real-time Feedback**: Angular UI provides instant strength assessment

✅ **Comprehensive Analysis**: Evaluates length, character diversity, entropy, and more

✅ **API Ready**: Easy integration with any application via REST API

✅ **Open Source**: Fully customizable and extendable

✅ **Visual Feedback**: Color-coded strength indicators and probability scores

✅ **Scalable Architecture**: Modular design for easy maintenance

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **FastAPI** - Modern, fast web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **matplotlib** - Visualization

### Frontend
- **Angular 21.1.2** - TypeScript-based framework
- **Tailwind CSS** - Utility-first styling
- **RxJS** - Reactive programming
- **Vitest** - Testing framework

### Data Processing
- **Feature Engineering** - Custom password analysis
- **StandardScaler** - Feature normalization
- **GridSearchCV** - Hyperparameter tuning

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have:
- Python 3.8+
- Node.js 18+
- npm or yarn
- Docker (optional, for containerized deployment)

### Quick Start

#### Backend Setup

```bash
# Clone the repository
git clone https://github.com/kerfaiyass54/password_strength.git
cd password_strength

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Download the dataset (or provide your own)
# Place data.csv in the datasets/ directory
```

#### Frontend Setup

```bash
# Navigate to the frontend directory
cd password-strength-ui

# Install Angular dependencies
npm install

# Build the Angular application
npm run build
```

#### Run the Application

```bash
# Start the FastAPI backend in one terminal
uvicorn src.api:app --reload

# Start the Angular frontend in another terminal
cd password-strength-ui
ng serve
```

Now you can access:
- API: http://localhost:8000/docs (Swagger UI)
- Frontend: http://localhost:4200

---



## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```
# Dataset configuration
DATA_PATH=datasets/data.csv

# Model paths
MODEL_PATH=models/password_classifier.pkl
SCALER_PATH=models/scaler.pkl

# API configuration
API_HOST=0.0.0.0
API_PORT=8000
```

### Customization Options

1. **Model Parameters**: Modify `train.py` to adjust:
   - `param_grid` for hyperparameter tuning
   - Classifier type (currently RandomForest)
   - Feature engineering in `feature_engineering.py`

2. **Strength Categories**: Edit `config.py` to change:
   - `MIN_STRENGTH` and `MAX_STRENGTH`
   - Target column mapping

3. **UI Customization**: Modify Angular components in `password-strength-ui/src/app/password-checker/`

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kerfaiyass54/password_strength.git
cd password_strength

# Set up backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up frontend
cd password-strength-ui
npm install

# Run tests
cd ..
python -m pytest tests/  # If test files exist
cd password-strength-ui
ng test
```

### Code Style Guidelines

1. **Python**:
   - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
   - Use Black for code formatting
   - Write docstrings for all functions and classes

2. **TypeScript/Angular**:
   - Follow [Angular Style Guide](https://angular.io/guide/styleguide)
   - Use Prettier for code formatting
   - Write comprehensive component tests

3. **Commit Messages**:
   - Follow [Conventional Commits](https://www.conventionalcommits.org/)
   - Example: `feat: add password entropy calculation`

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'feat: add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request



## 🚀 Getting Started with Contributions

Ready to contribute? Here's how to get started:

1. **Good First Issues**: Check for issues labeled "good first issue"
2. **Documentation**: Help improve the README or add documentation
3. **Features**: Suggest new features in the discussions
4. **Bug Fixes**: Report and fix any issues you find

Every contribution helps make this project better! 🎉
