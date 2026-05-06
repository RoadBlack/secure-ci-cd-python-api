# Secure CI/CD Pipeline for a Containerized Python API

> A small Python API project built to practice modern CI/CD workflows, Docker-based delivery, automated testing, and security-first engineering.
---
## Overview

This project demonstrates how a simple containerized Python API can be delivered through a secure and automated CI/CD pipeline.

The goal is not only to build an really simple application, but to design a delivery process that reflects a secure SDLC mindset: every change should be tested, scanned, verified, and only then considered ready for deployment.

The project focuses on practical DevSecOps fundamentals:

- automated API testing
- Docker image building
- secret scanning
- static application security testing
- container vulnerability scanning
- security gates in CI/CD
---
## Project Goal

The main goal of this project is to build a secure CI/CD pipeline for a simple Python API packaged as a Docker container.

This repository is intended as a learning and practice project for:

- CI/CD pipeline design
- Docker and containerization
- automated quality checks
- security scanning in CI
- secure software delivery habits
---
## What This Project Demonstrates

| Area | Description |
|---|---|
| CI/CD | Automated pipeline that validates code before build or deployment |
| Docker | API packaged into a reproducible container image |
| Automated Testing | Tests verify basic API behavior before the pipeline continues |
| Secret Scanning | Checks for accidentally committed credentials or sensitive values |
| SAST | Static analysis helps detect insecure code patterns |
| Container Scanning | Docker image is scanned for known vulnerabilities |
| Security Gates | Pipeline can fail when security or quality requirements are not met |
| Secure SDLC | Security is treated as part of the development workflow, not an afterthought |
---
## Why This Project Exists

A working application is only one part of software delivery.

Modern engineering also requires confidence that the application can be built, tested, scanned, and shipped in a consistent way. This project was created to practice that full lifecycle on a small, understandable codebase.

Instead of focusing on application complexity, the project focuses on the delivery process around it.
---
## Architecture

```text
Developer
   |
   | push / pull request
   v
CI/CD Pipeline
   |
   |-- run automated tests
   |-- scan repository for secrets
   |-- run static security analysis
   |-- build Docker image
   |-- scan container image
   |
   v
Validated Containerized API