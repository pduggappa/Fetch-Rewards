# Fetch-Rewards
Fetch Rewards Text Similarity

Introduction:
This is a simple Flask web application that takes in 2 pieces of texts and spits out the percentage of similarity between the 2 texts.
The algorithm is no way near perfect. It needs much more refinement, but, it is a very good starting point.

Considerations:
Punctuated words will be substituted for their original. I have used a punctuation dict from https://gist.github.com/nealrs/96342d8231b75cf4bb82 that has a dict of many punctuations and their extended form. I have included this as a json file, so this can be expanded upon further by anyone in the future.
Repetitive words don't add to similarity. I will be using a set, so duplicate words will not count.
I have used a library called 'Inflect', which converts numerals into spoken word(ex: 1 -> one, 2 -> two and so on.), so digit to text conversion is covered.
Special characters are ignored.
Ordering of the words do not matter.

Algorithm:
The actual algorithm is a replica of the Cosine Similarity algorithm. Here are the steps:

Get the 2 texts from the User.
Tokenize the texts - convert the text into a list of words. Here's where we expand the punctuations and substitute the digits with actual text.
Once the text is tokenized and we are left with a list of words for each text, we remove duplicates by converting it to a set.
We create an 'All Words' vector by taking the union of these 2 sets.This vector has words from both text 1 and text 2.
Now, we create 2 new lists that have 1 for every word in text 1 that is present in text 2. If not, we substitute it with 0.
For every word in both texts, we find the cosine similarity using the following formula :
similarity = similarity + word in text 1(1 or 0) x word in text 2 (1 or 0)
cosine_similarity = similarity / (sum of common words from text 1 in text 2 x sum of common words from text 2 in text 1) power of 0.5
This will give us a good idea if the 2 texts are similar or not.

Source Code:
This web app consists of the following files:
    src
        templates
            Homepage.html
        app.py
        Dockerfile
        punctuations.json
        Readme.md
        requirements.txt

Running the app:
The app completes the bonus requirements too, so this would be a Flask web app that has been Dockerized.
To run the app, use the follow commands:
    docker build -t IMAGE_NAME .
    docker run --name IMAGE_NAME -p 5001:5001 IMAGE_NAME
Go to http://0.0.0.0:5001/ and enter the texts to find the similarity.
