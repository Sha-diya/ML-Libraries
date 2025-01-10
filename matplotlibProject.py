import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    x=np.linspace(0,10,100)
    y=np.sin(x)
    plt.plot(x,y,label='sin(x)',color='blue')
    plt.title("Line plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()
    
    
def bar_plot():
    catagories=["A","B","C","D"]
    values=[2,3,5,7]
    plt.bar(catagories,values,color='purple')
    plt.title("Bar Plot")
    plt.xlabel("Catagories")
    plt.ylabel("Values")
    plt.show()
    
    
def scatter_plot():
    x=np.random.randn(100)
    y=np.random.randn(100)
    plt.scatter(x, y, c="green",alpha=0.6)
    plt.title("Scatter Plot")
    plt.xlabel("x-axis")
    plt.ylabel("Y-axis")
    plt.show()
    
def histogram_plot():
    data=np.random.randn(100)
    plt.hist(data, bins=20,color="orange",edgecolor="black")
    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()
    
    
def pie_chart():
    labels=["A","B","C","D"]
    values=[20,30,40,10]
    plt.pie(values,labels=labels,autopct="%1.1f%%",startangle=90)
    plt.title("Pie chart")
    plt.show()
    
    
def filled_area_plot():
    x=np.linspace(0,10,100)
    y1=np.sin(x)
    y2=np.sin(x)+1
    plt.fill_between(x, y1,y2,color="lightblue",label="Filled Area")
    plt.plot(x,y1,color="blue",label="y1=sin(x)")
    plt.plot(x,y2,color="green",label="y2=sin(x)+1")
    plt.title("Filled area plot")
    plt.legend()
    plt.show()
    
    
def step_plot():
    x=np.linspace(0, 10, 20)
    y=np.exp(x/10)
    plt.step(x,y,label="Step Function",color="orange",where="mid")
    plt.title("Step Function")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()
    
    
def error_bar_plot():
    x=np.arange(1,11)
    y=2*x + np.random.normal(0,1,10)
    error=np.random.uniform(0.5,1.5,size=len(x))
    plt.errorbar(x, y, yerr=error,fmt="o",ecolor="red",capsize=5,label="data with errors")
    plt.title("Error Bar")
    plt.legend()
    plt.show()
    
    
def multiple_lines_plot():
    x=np.linspace(0,10, 100)
    plt.plot(x,np.sin(x),label="sin(x)",color="blue")
    plt.plot(x,np.cos(x),label="cos(x)",color="green")
    plt.legend()
    plt.show()
    
    
    
def heatmap():
    data=np.random.randint(1,10,size=(5,5))
    plt.imshow(data, cmap="coolwarm",interpolation="nearest")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            plt.text(j, i, f"{data[i,j]}", ha="center",va="center",color="black")
    plt.colorbar(label="Values")
    plt.show()
    
    
def violin_plot():
    data=[np.random.normal(0,std,100) for std in range(1,4)]
    plt.violinplot(data,showmeans=True)
    plt.title("Violin Plot")
    plt.xticks([1,2,3],["Group 1","Group 2","Group 3"])
    plt.ylabel("Values")
    plt.grid()
    plt.show()
    
    
def radar_chart():
    categories = ["A","B","C","D","E"]
    values=[2,4,1,4,7]
    angles=np.linspace(0,2* np.pi, len(categories),endpoint=False).tolist()
    values+=values[:1]
    angles+=angles[:1]
    plt.figure(figsize=(6,6))
    ax=plt.subplot(111, polar=True)
    ax.fill(angles, values, color="blue",alpha=0.25)
    ax.plot(angles, values, color="blue",linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title("Rader chart")
    plt.show()
    
    
def threeD_plot():
    fig=plt.figure()
    ax=fig.add_subplot(111,projection="3d")
    x=np.random.randn(100)
    y=np.random.randn(100)
    z=np.random.randn(100)
    ax.scatter(x,y,z,cmap="viridis",marker="o",alpha=0.8)
    ax.set_title("3D scatter plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    plt.show()
    
def display_menu():
    print("Matplotlib Examples Project")
    print("1. Line Plot")
    print("2. Bar Plot")
    print("3. Scatter Plot")
    print("4. Histogram")
    print("5. Pie Chart")
    print("6. Filled Area Plot")
    print("7. Step Plot")
    print("8. Error Bar Plot")
    print("9. Multiple Lines Plot")
    print("10. Heatmap")
    print("11. Violin Plot")
    print("12. Radar Chart")
    print("13. 3D Plot")
    print("0. Exit")
    
    
if __name__=="__main__":
    while True:
        display_menu()
        choise=int(input("Enter your choice(0 to exit): "))
        if choise==0:
            print("Exitting the project.\n Good bye!")
            break
        
        elif choise==1:
            print("1. Line Plot")
            line_plot()
            
        elif choise==2:
            print("2. Bar Plot")
            bar_plot()
            
        elif choise==3:
            print("3. Scatter Plot")
            scatter_plot()
            
        elif choise==4:
            print("4. Histogram")
            histogram_plot()
            
        elif choise==5:
            print("5. Pie Chart")
            pie_chart()
            
        elif choise==6:
            print("6. Filled Area Plot")
            filled_area_plot()
            
        elif choise==7:
            print("7. Step Plot")
            step_plot()
            
        elif choise==8:
            print("8. Error Bar Plot")
            error_bar_plot()
            
        elif choise==9:
            print("9. Multiple Lines Plot")
            multiple_lines_plot()
            
        elif choise==10:
            print("10. Heatmap")
            heatmap()
            
        elif choise==11:
            print("11. Violin Plot")
            violin_plot()
            
        elif choise==12:
            print("12. Radar Chart")
            radar_chart()
            
        elif choise==13:
            print("13. 3D Plot")
            threeD_plot()
            
        else:
            print("Invalid input")