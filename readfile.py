import traceback
try:
    contributor = {}
    f = open('a_an_example.in.txt','r')

    num_contributors,num_projects = f.readline().split()

    # Extracting names of contributors as well as skill and their levels
    for i in range(int(num_contributors)):
        name,num_skills = f.readline().split()
        contributor[name] = {}
        for j in range(int(num_skills)):
            skill,level = f.readline().split()
            contributor[name][skill] = int(level)

    # printing the names of contributor and skills follwed by their level
    print("Contributor ",contributor)

    proj = {}
    for i in range(int(num_projects)):
        project_name , duration , points , best_bef , no_of_cont=f.readline().split()
        proj[project_name] = {}
        proj[project_name]['skills'] = {}
        proj[project_name]['duration'] = duration
        proj[project_name]['points'] = points
        proj[project_name]['bestbef'] = best_bef
        proj[project_name]['noofcont'] = no_of_cont
        for j in range(int(no_of_cont)):
            skill_req,lvl_req = f.readline().split()
            proj[project_name]['skills'][skill_req] = int(lvl_req)
    print("\n Project\n",proj)

    


except Exception:
    traceback.print_exc()
