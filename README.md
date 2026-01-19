# Mini RAG App

A simple backend application built with FastAPI and MongoDB as a foundation for a Retrieval-Augmented Generation (RAG) system.

## Overview

This project provides a basic backend structure for managing projects and preparing data to be processed later as chunks.  
Each project represents a logical unit (such as a document or dataset) that can contain multiple chunks.

The system automatically creates a project if it does not already exist.

## Tech Stack

- Python
- FastAPI
- MongoDB
- Motor (Async MongoDB Driver)
- Pydantic
- Docker & Docker Compose

## Database

- Database name: `mini_rag`
- Collections:
  - `projects` – stores project metadata
  - `chunks` – stores data chunks related to each project
## Run the Project

- $ uvicorn main:app --reload --host 0.0.0.0 --port 5000

## Purpose

This project is built for learning and experimentation with:
- FastAPI
- Async MongoDB operations
- Clean backend architecture
- Preparing data pipelines for RAG systems



