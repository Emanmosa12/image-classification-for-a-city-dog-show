#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Eman Mousa
# DATE CREATED: 02.03.2025
# REVISED DATE: 
# PURPOSE: Prints summary statistics from results_stats_dic and misclassified 
#          cases from results_dic if specified by user.

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints classification results summary and, if requested, misclassified dogs 
    and misclassified dog breeds.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List:
                    idx 0: Pet image label (string)
                    idx 1: Classifier label (string)
                    idx 2: 1/0 (int) - Match between pet & classifier labels
                    idx 3: 1/0 (int) - Pet image 'is-a' dog
                    idx 4: 1/0 (int) - Classifier labels image 'as-a' dog
      results_stats_dic - Dictionary with results statistics (percentages/counts)
                          Key starts with 'pct' for percentage or 'n' for count.
      model - CNN model architecture used (string): 'resnet', 'alexnet', or 'vgg'.
      print_incorrect_dogs - Boolean, prints incorrectly classified dogs if True.
      print_incorrect_breed - Boolean, prints incorrectly classified breeds if True.
    
    Returns:
      None - Only prints the results.
    """
    # Print model used
    print("\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    
    # Print overall image statistics
    print(f"Total Images: {results_stats_dic['n_images']}")
    print(f"Total Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Total Non-Dog Images: {results_stats_dic['n_notdogs_img']}\n")
    
    # Print percentage-based statistics
    print("Model Performance Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):
            print(f"  {key}: {value:.2f}%")

    # Print misclassified dogs if requested
    if print_incorrect_dogs:
        incorrect_dogs = [fname for fname, vals in results_dic.items() if sum(vals[3:]) == 1]
        if incorrect_dogs:
            print("\nMisclassified Dogs:")
            for filename in incorrect_dogs:
                print(f"  Pet Label: {results_dic[filename][0]} | Classifier Label: {results_dic[filename][1]}")
        else:
            print("\nNo misclassified dogs found.")

    # Print misclassified breeds if requested
    if print_incorrect_breed:
        incorrect_breeds = [fname for fname, vals in results_dic.items() if vals[3] == 1 and vals[4] == 1 and vals[2] == 0]
        if incorrect_breeds:
            print("\nMisclassified Dog Breeds:")
            for filename in incorrect_breeds:
                print(f"  Pet Label: {results_dic[filename][0]} | Classifier Label: {results_dic[filename][1]}")
        else:
            print("\nNo misclassified dog breeds found.")

