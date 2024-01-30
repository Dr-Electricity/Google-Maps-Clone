import mapsFunctions
import tkinter as tk

client = mapsFunctions.googleMapsClient()

root = tk.Tk()
root.title('Google Maps')
root.geometry('500x500')

# the type ignore is because python is raising an error, but nothing is really wrong, so if i just add that it works

resultLabel1 = tk.Label(root, text='Result 1', wraplength=100)
resultLabel2 = tk.Label(root, text='Result 2', wraplength=100)
resultLabel3 = tk.Label(root, text='Result 3', wraplength=100)
resultLabel4 = tk.Label(root, text='Result 4', wraplength=100)

query = tk.Entry(root, width=30)



def search():
    client.queryAutocomplete(f'{query.get()} in Amman, Jordan')
    resultLabel1.config(text=client.places[1][0])
    resultLabel2.config(text=client.places[2][0])
    resultLabel3.config(text=client.places[3][0])
    resultLabel4.config(text=client.places[4][0])

def place1():    
    try:
        (businessStatus,), (formattedAddress,), (name,), (phoneNumber,), (openingHours,), (rating,), (mapsUrl,) = client.getPlaceDetails(1) # type: ignore
    except(ValueError):
        result = "Invalid option. Please choose another location"
        resultWindow = tk.Toplevel(root)
        resultDetailLabel = tk.Label(resultWindow, text='')
        resultDetailLabel.config(text=result)
        resultDetailLabel.pack()
        return result
    pass
    result = businessStatus + formattedAddress + name + phoneNumber + openingHours + rating + mapsUrl 
    resultWindow = tk.Toplevel(root)
    resultDetailLabel = tk.Label(resultWindow, text='')
    resultDetailLabel.config(text=result)
    resultDetailLabel.pack()
    return result

def place2():
    try:
        (businessStatus,), (formattedAddress,), (name,), (phoneNumber,), (openingHours,), (rating,), (mapsUrl,) = client.getPlaceDetails(2) # type: ignore
    except(ValueError):
        result = "Invalid option. Please choose another location"
        resultWindow = tk.Toplevel(root)
        resultDetailLabel = tk.Label(resultWindow, text='')
        resultDetailLabel.config(text=result)
        resultDetailLabel.pack()
        return result
    pass 
    result = businessStatus + formattedAddress + name + phoneNumber + openingHours + rating + mapsUrl 
    resultWindow = tk.Toplevel(root)
    resultDetailLabel = tk.Label(resultWindow, text='')
    resultDetailLabel.config(text=result)
    resultDetailLabel.pack()
    return result

def place3():
    try:
        (businessStatus,), (formattedAddress,), (name,), (phoneNumber,), (openingHours,), (rating,), (mapsUrl,) = client.getPlaceDetails(3) # type: ignore
    except(ValueError):
        result = "Invalid option. Please choose another location"
        resultWindow = tk.Toplevel(root)
        resultDetailLabel = tk.Label(resultWindow, text='')
        resultDetailLabel.config(text=result)
        resultDetailLabel.pack()
        return result
    pass
    result = businessStatus + formattedAddress + name + phoneNumber + openingHours + rating + mapsUrl 
    resultWindow = tk.Toplevel(root)
    resultDetailLabel = tk.Label(resultWindow, text='')
    resultDetailLabel.config(text=result)
    resultDetailLabel.pack()
    return result

def place4():
    try:
        (businessStatus,), (formattedAddress,), (name,), (phoneNumber,), (openingHours,), (rating,), (mapsUrl,) = client.getPlaceDetails(4) # type: ignore
    except(ValueError):
        result = "Invalid option. Please choose another location"
        resultWindow = tk.Toplevel(root)
        resultDetailLabel = tk.Label(resultWindow, text='')
        resultDetailLabel.config(text=result)
        resultDetailLabel.pack()
        return result
    pass
    result = businessStatus + formattedAddress + name + phoneNumber + openingHours + rating + mapsUrl 
    resultWindow = tk.Toplevel(root)
    resultDetailLabel = tk.Label(resultWindow, text='')
    resultDetailLabel.config(text=result)
    resultDetailLabel.pack()
    return result

queryButton = tk.Button(root, text='Search', command=search)

resultButton1 = tk.Button(root, text='Get Details', command=place1)
resultButton2 = tk.Button(root, text='Get Details', command=place2)
resultButton3 = tk.Button(root, text='Get Details', command=place3)
resultButton4 = tk.Button(root, text='Get Details', command=place4)

resultLabel1.grid(row=0, column=0, padx=3, pady=10)
resultLabel2.grid(row=1, column=0, padx=3, pady=10)
resultLabel3.grid(row=2, column=0, padx=3, pady=10)
resultLabel4.grid(row=3, column=0, padx=3, pady=10)

resultButton1.grid(row=0, column=2, padx=3, pady=10)
resultButton2.grid(row=1, column=2, padx=3, pady=10)
resultButton3.grid(row=2, column=2, padx=3, pady=10)
resultButton4.grid(row=3, column=2, padx=3, pady=10)

query.grid(row=4, column=0, padx=3, pady=10)
queryButton.grid(row=4, column=2, padx=3, pady=10)


root.mainloop()