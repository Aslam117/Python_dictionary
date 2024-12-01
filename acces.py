thisdic={
    "brand" :"ford",
    "model": "mustang",
    "year": 1964
}
print(thisdic)
x=thisdic["year"]
print(x)

y=thisdic.values()
print(y)
z=thisdic.items()
print(z)
thisdic["year"]=2000
print(thisdic)