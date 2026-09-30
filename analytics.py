import pandas as pd



def calculate_results(data):
     data = data.copy()


      subjects = ["Maths", "Science", "English"]
    
       data["Total"] = data[subjects].sum(axis=1)

       data["Percentage"] = data["Total"] / 3

       data["Percentage"] = data["Percentage"].round(2)

       data["Grade"] = data["Percentage"].apply(assign_grade)
     
       data["Result"] = data[subjects].apply( lambda row: "Pass" if all(row >= 40) else "Fail",
              axis=1
         )

         return data

        def assign_grade(percentage):
            if percentage >= 90:
               return "A+"
            elif percentage >= 80:
                return "A"
            elif percentage >= 70:
                 return "B"
            elif percentage >= 60:
                 return "C"
            elif percentage >= 50:
                 return "D"
            elif percentage >= 40:
                 return "E"
            else:
                 return "F"

           
           def subject_average(data):
               subjects = ["Maths", "Science", "English"]
               return data[subjects].mean().round(2)


           def top_students(data, n=5):
               data = calculate_results(data)

               return data.sort_values(
                  by="Percentage",
                  ascending = False
                ).head(n)


           def find_students(data, student_id):
               data = calculate_results(data)

               result = data[
                        data["Student ID"].astype(str).str.upper()
                        == str(student_id).upper()
              ]
        
              return result
           
             
