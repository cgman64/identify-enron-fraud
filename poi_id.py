#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit

financial_features = ['salary', 'deferral_payments', 'total_payments', 
                      'loan_advances', 'bonus', 'restricted_stock_deferred', 
                      'deferred_income', 'total_stock_value', 'expenses', 
                      'exercised_stock_options', 'other', 
                      'long_term_incentive', 'restricted_stock', 
                      'director_fees'] # all units are in US dollars.

email_features = ['to_messages', 'email_address', 'from_poi_to_this_person', 
                  'from_messages', 'from_this_person_to_poi', 
                  'shared_receipt_with_poi'] # units are generally number of 
                                             # emails messages; notable 
                                             # exception is ‘email_address’, 
                                             # which is a text string.

poi_label = ['poi'] # boolean 1 for person of interest, 0 for not.

features_list = poi_label + financial_features + email_features

print features_list




