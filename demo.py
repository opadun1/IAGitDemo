import pandas as pd

data = {
    'FirstName': ["Artem", "Syed","Oleksii"],
    'LastName': ["Frenk", "Shazli", "Padun"],
    'Year': ['Sophomore', 'Sophomore', 'PhD 2']    

}
df = pd.DataFrame(data)
csv_name = "names.csv"
df.to_csv(csv_name, index = False)
print (f'Data saved to {csv_name}')