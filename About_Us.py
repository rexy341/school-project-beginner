# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:09:29 2023

@author: Net
"""
import pickle

f = open(r"AboutUs.dat", "wb")

strg = """
Welcome to Bal Bharati Public School Navi Mumbai
Bal Bharati Public School, Navi Mumbai, would like to be evaluated, rated on the hopefulness 
and confidence exhibited, today and later, by its students and on their ability to retain 
purpose in life long after the sweet school days are over.  The schools aims to provide the
right mix of exposure to knowledge, of opportunities to test and hone various personal skills,
and of competitions to partake and self-realise to each and every one student.      

Bal Bharati Public School, Navi Mumbai, is a constituent unit of the Child Education Society 
(CES), Delhi.The CES is registered under the Societies’ Registration Act 1860, and was founded 
in 1944 by eminent personalities.Our school aims at sustaining an environment wherein students 
can excel in scholastic activities, demonstrate superior learning, and develop intellectual 
capacities and skills that prepare them for service to the society.We aim to make the young learners
to appreciate the true wonders of our world and never to stop thirsting for more in this direction.
We also aim to have among teachers, principal, parents and community residents a mutually 
beneficial, symbiotic relationship based on trust and cooperation.Bal Bharati Public School, 
Navi Mumbai, strives to provide students with rich and deep learning experiences.The school
makes every effort to provide students with numerous avenues of advancement, and train them to 
learn, unlearn and relearn as they progress so that they are ever on par with time.  Forming 
healthy relationships, social and emotional resilience and having a sense of awe at the beauty 
around us are some of the things that we actively encourage our students to learn and retain.
Besides academic excellence and intellectual development, Bal Bharati Public School, Navi Mumbai,
endeavours to help each child discover and develop their innate talents and abilities.  It seeks
to instil in children proper habits, positive attitudes and values such as truthfulness, unselfishness
, self-respect, sense of duty, discipline, striving for excellence, cleanliness, civic sense, fair 
play and team-spirit, dignity of labour, and a lot more.On account of its healthy aims and objectives
and continuous efforts to do better and better at every step and every day, Bal Bharati Public School
, Navi Mumbai, is one of the most sought after schools in all of Navi Mumbai for many years now.
We are confident of retaining the prime place we have secured through hard work over the years.  
We remain committed to the timeless journey towards higher and higher standards of excellence.


Address: PLOT NO 5, Sector 4, Kharghar, Navi Mumbai, Maharashtra 410210
Phone Number:+91 (022) 27741641, 27742773
Email: bbpskhrnm@yahoo.com

School Timings: 7:50am - 2:30pm
Working Days: Monday-Friday    

"""

pickle.dump(strg, f)
f.close()
