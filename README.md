#  Autism Screening Tool

A web‑based application that leverages machine learning to provide a fast, accessible, and user‑friendly preliminary assessment of Autism Spectrum Disorder (ASD) risk. Built with Streamlit and Python, this tool allows non‑specialists—parents, teachers, community health workers—to complete a standardized questionnaire and receive an immediate probabilistic estimate of ASD likelihood.  

> **⚠️ Disclaimer:** This tool is **not** a substitute for professional clinical diagnosis. It is intended only as a screening aid to flag individuals who may benefit from a full diagnostic evaluation.

---

## 📋 Table of Contents

1. [Motivation & Overview](#motivation--overview)  
2. [Features](#features)  
3. [Architecture & Workflow](#architecture--workflow)  
4. [Data & Model](#data--model)  
5. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Running the App](#running-the-app)  
6. [Usage](#usage)  
7. [Performance](#performance)  
8. [Future Enhancements](#future-enhancements)  
9. [License](#license)  
10. [Acknowledgments](#acknowledgments)  

---

## Motivation & Overview

Early intervention in Autism Spectrum Disorder (ASD) dramatically improves long‑term outcomes. Traditional diagnostic pathways (e.g., ADOS, ADI‑R) require specialized clinicians and can take months. Our AI‑Powered Autism Screening Tool bridges this accessibility gap by:

- Automating the initial screening process  
- Delivering real‑time feedback via a simple web interface  
- Reducing bottlenecks in regions with limited clinical resources  

---

## Features

- **Standardized Questionnaire**: Built on validated behavioral indicators for ASD  
- **Real‑Time Prediction**: Instant risk score as soon as the form is submitted  
- **User‑Friendly UI**: Intuitive Streamlit interface—no coding required  
- **Lightweight Deployment**: Runs in any modern browser; deployable on Heroku, AWS, Azure, etc.  
- **Exportable Reports**: Downloadable summary of responses and risk score  

---

## Architecture & Workflow

```mermaid
flowchart LR
  A[User opens web app] --> B[Complete questionnaire]
  B --> C[Responses sent to ML model]
  C --> D[Model predicts ASD risk probability]
  D --> E[Display risk score & summary]
  E --> F[Option to download report]

