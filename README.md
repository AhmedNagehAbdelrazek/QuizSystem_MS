# Quiz System Documentation

#### Overview
This document provides an overview of the Quiz System architecture, including the key entities, their relationships, and the API endpoints. This system is designed to be a microservice, with user authentication handled by an external HR Management System.

---

#### Table of Contents
1. [System Architecture](#system-architecture)
2. [Entities and Relationships](#entities-and-relationships)
3. [Django Models](#django-models)
4. [API Endpoints](#api-endpoints)
5. [Validation and Constraints](#validation-and-constraints)
6. [Indexing](#indexing)
7. [Testing](#testing)
8. [Documentation](#documentation)

---

### System Architecture

---

### Entities and Relationships

1. **Questions**
    - `id` (Primary Key, auto-incremented)
    - `description` (string): The question text.
    - `type` (string): Enum with values ('text', 'options', 'code').
    - `is_answer_required` (boolean): Indicates if the question has a correct answer.
    - `test_cases` (JSON): Array of objects containing input and output.
    - `options` (JSON): Array of strings containing options.
    - `correct_answer` (string): The correct answer if applicable.
    - `author_id` (ForeignKey to User): Reference to the user who wrote the question.
    - `is_public` (boolean): Indicates if the question is public or private.
    - `created_at` (DateTime): Timestamp when the question was created.
    - `updated_at` (DateTime): Timestamp when the question was last updated.

2. **Quizzes**
    - `id` (Primary Key, auto-incremented)
    - `name` (string): The name of the quiz.
    - `questions` (ManyToManyField to Question through QuizQuestion): The questions in the quiz.
    - `is_public` (boolean): Indicates if the quiz is public or private.
    - `time_limit` (integer): Time limit in minutes to complete the quiz.
    - `author_id` (ForeignKey to User): Reference to the user who created the quiz.
    - `created_at` (DateTime): Timestamp when the quiz was created.
    - `updated_at` (DateTime): Timestamp when the quiz was last updated.

3. **QuizQuestions** (Intermediary Table)
    - `quiz_id` (ForeignKey to Quiz)
    - `question_id` (ForeignKey to Question)
    - `is_mandatory` (boolean): Indicates if the question is mandatory in the quiz.

4. **Applications**
    - `id` (Primary Key, auto-incremented)
    - `user_id` (ForeignKey to User): Reference to the user who is taking the quiz.
    - `quiz_id` (ForeignKey to Quiz): Reference to the quiz being taken.
    - `start_time` (DateTime): Time when the user started the quiz.
    - `end_time` (DateTime): Time when the user completed the quiz.
    - `created_at` (DateTime): Timestamp when the application was created.
    - `updated_at` (DateTime): Timestamp when the application was last updated.

5. **Answers**
    - `id` (Primary Key, auto-incremented)
    - `question_id` (ForeignKey to Question): Reference to the question being answered.
    - `application_id` (ForeignKey to Application): Reference to the application.
    - `answer_text` (string): The user's answer.
    - `is_correct` (boolean): Indicates if the answer is correct (only applicable for questions with correct answers).
    - `created_at` (DateTime): Timestamp when the answer was submitted.
    - `updated_at` (DateTime): Timestamp when the answer was last updated.


### API Endpoints

#### Authentication
- Handled by the HR Management System.

#### Question Endpoints
- **GET /questions/**: List all questions.
- **POST /questions/**: Create a new question.
- **GET /questions/{id}/**: Retrieve a question by ID.
- **PUT /questions/{id}/**: Update a question by ID.
- **DELETE /questions/{id}/**: Delete a question by ID.

#### Quiz Endpoints
- **GET /quizzes/**: List all quizzes.
- **POST /quizzes/**: Create a new quiz.
- **GET /quizzes/{id}/**: Retrieve a quiz by ID.
- **PUT /quizzes/{id}/**: Update a quiz by ID.
- **DELETE /quizzes/{id}/**: Delete a quiz by ID.

#### Application Endpoints
- **GET /applications/**: List all applications.
- **POST /applications/**: Create a new application.
- **GET /applications/{id}/**: Retrieve an application by ID.
- **PUT /applications/{id}/**: Update an application by ID.
- **DELETE /applications/{id}/**: Delete an application by ID.

#### Answer Endpoints
- **GET /answers/**: List all answers.
- **POST /answers/**: Submit a new answer.
- **GET /answers/{id}/**: Retrieve an answer by ID.
- **PUT /answers/{id}/**: Update an answer by ID.
- **DELETE /answers/{id}/**: Delete an answer by ID.


### Validation and Constraints

1. **Question Model**:
    - Ensure `type` is one of ('text', 'options', 'code').
    - If `type` is 'options', `options` field must be non-empty.
    - If `is_answer_required` is True, `correct_answer` must be provided.

2. **Quiz Model**:
    - Ensure `time_limit` is a positive integer.
    - Ensure `name` is unique per author.

3. **Application Model**:
    - Ensure `end_time` is greater than `start_time`.
