#!/bin/bash
# Write a script to solicit "You got me!"
curl -s -L -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: You got me!"
