# sample-setup

__Quick disclaimer:__

The files here are all thrown together in a haphazard mess because I was just trying to get all three things working without much regard to them interacting with each other. In reality, a lot of cleaning up could be done here (although some things naturally cause issues - the \_\_test__ directory is necessary for jest, but trying to put the python test in there will cause a lot of difficulties. Even if I can figure it out (which I couldn't, see \#troubleshooting in the discord), I doubt students could)



Explanation of things:

  ### Spellchecker -
  
  Here, we use a community-made action to scan .md files (this can be changed) for spelling errors. Additionally, we use a wordlist.txt to add additional words of our choosing to the list of valid words. Detected misspellings are outputted in the test log, and the test will fail. My sample .md file has some butchered Hamlet quotes, so that we can make use of the custom wordlist.txt to help it decipher between typos and oddly spelt names. For a real implementation, maybe find something more topical than Hamlet, but I like the idea of forcing them to differentiate between genuine typos and relevant jargon.
  
   ### Pytest -
  
  This one also uses community-made actions to implement pytest, which is a useful test runner thanks to the relative simplicity of its test files. It has a few odd "must follow or this will break your code" steps, but nothing unfixable, meaning it could make for good independent study on the students' parts - self-troubleshooting is a necessary skill to have. I stole some random simple fibonacci sequence function from a website and wrote a 2 function test because I was lazy, but doing something more complex would be easy enough. This one is definitely more accessible than the jest one - I could see a student writing, or at least filling in the blanks, on the code for a python test than a javascript one.
  
   ### Jest -
  
  Jest can be utilized without any community actions, actually, so we've gone ahead and done that here. The actual function and associated test were taken from a jest tutorial I found online, since they wrote things in a pretty easy to parse way even if you don't know javascript. For example, I do not know javascript and I could read what was going on. For real implementation, maybe have more relevant code that interacts with the python in some way (or not - they could be two completely separate things. Grouping this separately from the python and spellchecker could make sense if we decide to focus the other two on a "how to implement community actions" sorta thing. It's not a hard thing to do, but it might be conceptually "out there" enough to warrant its own assignment)
  
  
  
  
  ## Week by week timeline - 
  
  These topics could probably cover two weeks, with...
  
  __Week 1 Project/Homework: Jest implementation__
  
  Jest's implementation is not only built in to GitHub actions, but is very similar to the workflow used in parts 1 and 2 of the learning lab tutorials. Starting with a softball. The specific javascript code I'm unsure of, since I don't know javascript, but I can get help with that. A very basic concept for a website maybe? 
  
  __Week 2 Project/Homework: Pytest + Spellchecker__
  
  Grouping together the two community-based actions, since they might require some troubleshooting for students to implement. Not difficult per se, but some of the steps to get these actions working as intended can be finicky, and hints might be offered throughout the week to address this. Maybe this could actively integrate the two things into a single project? Have the python manipulate a .md or .txt file that then gets spellchecked? Might be a bit cute. We could have the python do something involving website design and then spellcheck the contents of the page - again, would need help realizing this.
  
  
  
The livestream format would be pretty straight forward -
  1. intro
  2. covering the prior week's project and taking questions/troubleshooting
  3. supplemental material relevant to lessons (if any) 
  4. lessons
  5. go over the next week's project
  
 Week 1 would cover lessons 1 and 2, week 2 would cover lessons 3, 4, and 5 (pending the consolidation of 4 and 5 - they're quite similar), and week 3 would cover 6 and 7. 

### credits (maybe incomplete? I made this after the fact and might have forgotten some stuff):

https://github.com/marketplace/actions/run-pyspelling-as-a-github-action

https://www.valentinog.com/blog/jest/

https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions

https://realpython.com/python-testing/#writing-your-first-test

https://www.programiz.com/python-programming/examples/fibonacci-recursion
