import json
import tarfile
import os.path
 
 
with open( "./checkbox_submission_technical_assignment/submission.json" , "r") as fff:
     text = fff.read()
     
input_jason_file = json.loads(text)
distribution_dict = input_jason_file.get('distribution')
distributor_id = distribution_dict.get('distributor_id')
release = distribution_dict.get('release')
#print('Version tested : ', distributor_id, 'version', release)

print('The results are as below :')

store_list = []
pass_list = []
fail_list = []
skip_list = []
n = int(0)      # Number of the pass
m = int(0)      # Number of the fail
p = int(0)      # Number of the skip
q = int(0)      # Number of test run
d = float(0)    # duration time

result_array = input_jason_file.get('results')
for item in result_array:
    store_details = {}
    pass_details = {}
    fail_details = {}
    skip_details = {}
    
    store_details['id'] = item['id']
    store_details['status'] = item['status']
    store_details['duration'] = item['duration']
    print('-------------------------------------------------')
    print('id is', store_details['id'])
    print('status is', store_details['status'])
    print('duration is', store_details['duration'],'seconds')
       
#    store_list.append(store_details)
#    print(store_list)   
   
    if item['status'] == 'pass':
        n = n+1
        pass_list.append(store_details['id'])
 
    if item['status'] == 'fail':
        m= m+1
        fail_list.append(store_details['id']) 
   
    if item['status'] == 'skip':
        p = p+1
        skip_list.append(store_details['id'])
    
    d = d + float(item['duration'])
    q = n + m + p
    
print('Version tested : ', distributor_id, 'version', release)    
print('Number of tests run =', q)
print('Outcome :')
print('Total of pass =', n,'   (',' {:.0f}%'.format(n/q*100),' )')    
print('Total of fail =', m,'   (',' {:.0f}%'.format(m/q*100),' )') 
print('Total of skip =', p,'  (',' {:.0f}%'.format(p/q*100),' )') 
print('Total duration =',d, 'seconds') 
print('List of fail tests :', fail_list)


#Output JSON file
filename = "submission_report.json"
JsonObject = {
    distributor_id :  release ,
    "Nb_pass" : n,
    "Nb_fail" : m ,
    "Nb_skip" : p ,
    "Total duration" : d ,
    "Failed_Tests" : fail_list
}
file = open(filename, 'w')
json.dump(JsonObject, file)
file.close()


#Output txt file   
f = open('./submission_report.txt','w')
print('Version tested : ', distributor_id, 'version', release, file=f)    
print('Number of tests run =', q, file=f)  
print('Outcome :', file=f)  
print('Total of pass =', n,'   (',' {:.0f}%'.format(n/q*100),' )', file=f)    
print('Total of fail =', m,'   (',' {:.0f}%'.format(m/q*100),' )', file=f)   
print('Total of skip =', p,'  (',' {:.0f}%'.format(p/q*100),' )', file=f)   
print('Total duration =',d, 'seconds', file=f)  
print('List of fail tests :', fail_list, file=f)      
f.close()


#Output tar file
with tarfile.open("submission.tar.xz", "w:xz") as tar:
  for name in ["submission_report.json","submission_report.txt"]:
    tar.add(name)




#tar = tarfile.open("submission.tar.xz", "w:xz")
#for name in ["submission_report.json","submission_report.txt"]:
#    tar.add(name)
#tar.close()



 
