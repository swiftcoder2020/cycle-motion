<div>
   <img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0; padding-right: 15px;">
   <img src="learning-people-logo.png" style="margin: 0; padding-left: 15px; width: auto; height: 88px;">
</div>

# Cycle Motion
*Constructed as part of Code Institute's Milestone 3 Project: Python and Data Centric Development module*

## Introduction



## Demonstration

### **Responsive image of website**



**[Active link to Cycle Motion](#)**

## Table of Contents

1. [Overview](#overview)
2. [User Experience Design (UXD)](#user-experience-design)
   1. [Project Goals](#project-goals)
   2. [Strategy](#strategy)
   3. [Scope](#scope)
      - [User Stories](#user-stories)
      - [Features](#features)
         - [Future Features](#future-features)
   4. [Structure](#structure)
      - [Interaction Design (IXD)](#interaction-design)
      - [Information Architecture](#information-architecture)
      - [Sitemap](#sitemap)
   5. [Skeleton](#skeleton)
      - [Wireframing the Website](#wireframing-the-website)
   6. [Surface](#surface)
      - [Colour Palette](#colour-palette)
      - [Typography](#typography)
      - [Icons](#icons)
      - [Imagery](#imagery)
3. [Technologies Utilised](#technologies-utilised)
4. [Project Bugs and Solutions](#project-bugs-and-solutions)
5. [Testing](#testing)
   - [W3C Validator Tools](#w3c-validator-tools)
   - [JSHint](#jshint)
   - [PEP8 Online](#pep8-online)
   - [Responsive Tools](#responsive-tools)
   - [User Stories](#user-stories)
   - [General technical testing](#general-technical-testing)
6. [Deployment](#deployment)
   - [Initial Deployment](#initial-deployment)
   - [Fork a Repository](#fork-a-repository)
   - [Clone a Respository](#clone-a-repository)
   - [Generate a Local Clone](#generate-a-local-clone)
7. [Credits](#credits)
   - [Code](#code)
   - [Contents](#contents)
   - [Media](#media)
   - [Acknowledgements](#acknowledgements)

# Overview



# User Experience Design

## Project Goals



## Strategy



## Scope



### User Stories



### Features



#### Future Features



## Structure

### Interaction Design



### Information Architecture



### Sitemap



## Skeleton

## Wireframing the Website



## Surface

### Colour Palette



### Typography


### Icons



### Imagery



# Technologies Utilised

<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg" alt="HTML5 logo" width="50px" height="50px" />  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg" alt="CSS3 logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" alt="JavaScript logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/mongodb/mongodb-original-wordmark.svg" alt="MongoDB logo"
width="50px" height="50px" />

# Project Bugs and Solutions



# Testing

## W3C Validator Tools



## JSHint



## PEP8 Online



## Responsive Tools



## User Stories



## General Technical Testing



# Deployment

Given that the deployment of the previous second milestone project was based on GitHub Pages, 
which allows the hosting of static websites, the learning experience and skills of the 
subsequent module into Back-end Development have progressively transitioned whereby the language 
of Python will be adopted in this third milestone project therefore the hosting provider of 
Heroku is necessary as Python cannot be hosted on GitHub Pages.

## Initial Deployment

The development into this third milestone project had utilised the IDE of [GitPod](https://www.gitpod.io) which was subsequently pushed to the development community of [GitHub](https://www.github.com) and finally deployed using the recommended hosting provider of [Heroku](https://www.heroku.com). As a result of this, the following steps should be taken as specified below:

1. Create a file entitled as `requirements.txt` using the command of `pip3 freeze --local > requirements.txt` within the terminal of GitPod.
2. Using the same GitPod terminal, create a `Procfile` via the command of `echo web: python app.py > Procfile`.
3. Next, enter the command of either `git add.` or `git add -A` and then `git commit -m` the new requirements and Procfile files respectively before finally executing a `git push` to the GitHub repository.
4. Within the website of [Heroku](https://www.heroku.com), either Sign up or Log in where applicable.
5. Once you have signed up or logged in on Heroku, the creation of a new application is done through the click of the 'Create New App' button within your dashboard. Then choose a unique name and set the region that is closest to you e.g. Europe.
6. Within the dashboard of Heroku of your newly created application, click on "Deploy" > "Deployment method", then select "GitHub" and finally click the "Connect to GitHub" button.
7. Search for your correct GitHub repository name that you have created and confirm the linking up through a click on the "Connect" button.
8. Return back to your Heroku dashboard and click on "Settings" > "Reveal Config Vars".
9. Set the following config vars as:

| Key | Value |
| ----------|--------- |
| PORT | 5000 |
| IP | 0.0.0.0 |
| DEBUG | False |
| MONGO_URI | USER_MONGODB_URI |
| MONGO_DBNAME | USER_MONGODB_NAME |
| Secret_Key | USER_SECRET_KEY |

## Fork a Repository



## Clone a Respository



## Generate a Local Clone



# Credits



## Code



## Contents



## Media



## Acknowledgements

