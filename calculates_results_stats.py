#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the program run using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    results_stats_dic = dict()
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0 
    
    for key in results_dic:         
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1        
        
        #Pet Label is a dog & Labels match:
        #results_dic[key][3] = 1 and results_dic[key][2] = 1            
        if (results_dic[key][3] == 1) & (results_dic[key][2] == 1):
            results_stats_dic['n_correct_breed'] += 1
        
        # Pet Image Label is a Dog 
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1           
            # Classifier classifies image as Dog            
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        
        #and the classifier label indicates the images is-NOT-a-dog.
        if (results_dic[key][3] == 0) & (results_dic[key][4] == 0):
            results_stats_dic['n_correct_notdogs'] += 1
            
        results_stats_dic['n_images'] = len(results_dic)
        results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] -                                                                      results_stats_dic['n_dogs_img']) 
                
        if results_stats_dic['n_images'] > 0:
            aa = results_stats_dic['n_match']*100.0 / results_stats_dic['n_images'] 
        else:
            aa = 0.0
        results_stats_dic['pct_match'] =  aa
        
        if results_stats_dic['n_dogs_img'] > 0:
            bb = results_stats_dic['n_correct_dogs']*100.0 / results_stats_dic['n_dogs_img'] 
        else:
            bb = 0.0            
        results_stats_dic['pct_correct_dogs'] = bb
        
        if  results_stats_dic['n_dogs_img'] > 0:
            cc =  results_stats_dic['n_correct_breed']*100.0 / results_stats_dic['n_dogs_img'] 
        else:
            cc = 0.0
        results_stats_dic['pct_correct_breed'] = cc
        
        if results_stats_dic['n_notdogs_img'] > 0:
            dd = results_stats_dic['n_correct_notdogs']*100.0 / results_stats_dic['n_notdogs_img']
        else:
            dd = 0.0
        results_stats_dic['pct_correct_notdogs'] = dd
        
    return results_stats_dic
