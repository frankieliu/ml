Priyanka . 09:30 AM 
This jupyter notebook was covered in introduction to numpy video. Can you share the jupyter notebook also. It was not there.
Lijing Bu 09:51 AM 
Here is the ipynb, under the video  https://drive.google.com/drive/folders/1ledXv9FWP_zGfMHpvoILj-noWcTCmNTE?usp=drive_link
Janarthanan Subramani 09:32 AM  
May be this was discussed earlier - but why LIST isnt part of numpy and we switched to ARRAY ? Is it for perfrmance or more functionality ?
Bharath Pasupuleti 09:32 AM  
Can you please explain the use case of reshaping data to re-arrange data? What are the practical applications of reshaping?
Lijing Bu 09:56 AM 
When we want rows became columns :-)
Srividya Ananthasubramoney 09:37 AM  
data type int64 is how  diff from other ints in numpy?
Debobrata Dutta 09:43 AM 
Max and Min value will be different
Anurag Tripathy 09:41 AM  
Can we get median too in the same way? Like is there a function for that? If not, why not?
Anurag Tripathy 09:43 AM 
Thanks.
Senthilkumar Rajamanickam 09:43 AM  
Does multiply does automatic type conversion
IK Academic Support 09:43 AM 
Yes, NumPy's multiply function performs automatic type conversion
Raynard Kyle 09:44 AM  
What if the array is 2D, will multiplication still broadcast to all the elements?
IK Academic Support 09:44 AM 
Yes, if you multiply a 2D array by a scalar or another array with compatible dimensions, NumPy will broadcast the multiplication to all elements. The operation will apply element-wise across the entire 2D array.
Soumodeep Das 09:45 AM  
is there any class for statistics in ML in the course? Was wondering how impletement these np function for actual problem solving in ML
IK Academic Support 09:46 AM 
Please raise this query to ops team via chat. Alternatively, you can also sent us an email on operations@interviewkickstart.com
Sunil Sharma 09:46 AM  
can we go through some more examples of filter with shape > 1
IK Academic Support 09:48 AM 
Here are some examples:

Filtering Rows in a 2D Array:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered = arr[arr[:, 0] > 4]  # Filter rows where the first column > 4
# Result: array([[4, 5, 6], [7, 8, 9]])

Filtering Elements in a 3D Array:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
filtered = arr[arr > 5]  # Flatten and filter elements > 5
# Result: array([6, 7, 8])
venkat kasarla 09:51 AM  
when d we use just load as object with with .npy? how this object is saved
IK Academic Support 09:52 AM 
When you use np.load('filename.npy', allow_pickle=True) to load an object saved with .npy, it means the saved data is an arbitrary Python object, not just a NumPy array. This is useful when saving complex data structures like lists of dictionaries or other non-array objects.

The object is saved as a binary file in a format that retains its Python object structure, allowing you to load it back into Python in the same form it was saved.
venkat kasarla 09:53 AM 
Thank you
Priyanka . 09:52 AM  
c
This question has been answered live
Lakshmi Akkiraju 09:52 AM  
C
This question has been answered live
Sunil Sharma 09:52 AM  
Use Chat to answer
This question has been answered live
venkat kasarla 09:52 AM  
C
This question has been answered live
Aziz Milib 09:53 AM  
C
This question has been answered live
Balaji Raj 09:54 AM  
C
This question has been answered live
Naresh Kumar 09:57 AM  
D
This question has been answered live
Murali Bhojanapalli 09:58 AM  
C
This question has been answered live
Aziz Milib 09:58 AM  
Use Chat Please, dont you hear it
This question has been answered live
Murali Bhojanapalli 10:02 AM 
please be nice
Santosh Singh 10:03 AM 
so far we have been asked like 10 times to use chat. I don’t understand why we keep using the q&a?
Murali Bhojanapalli 10:19 AM 
it was an accident .. right..
no one does it on purpose
Srinivas Kruttiventi 09:58 AM  
D
This question has been answered live
Anurag Tripathy 10:04 AM  
Can you please explain the last option of the last quiz question again? The C and Fortran thing.
IK Academic Support 10:09 AM 
Sorry but can you please let us know which quiz you are referring to?
Anurag Tripathy 10:12 AM 
The question about why Arrays are faster than lists? The answer was option D. I also heard that on the pre-class mateial. But couldn’t really understand why?
The answer involved the fact that Arrays are implemented in C. Can u elaborate a bit on this?
IK Academic Support 10:15 AM 
Arrays are faster than lists because they are implemented in C, which allows for efficient, low-level operations, contiguous memory allocation, and type consistency. This results in faster computation and better performance compared to Python lists, which are more flexible but slower. The involvement of Fortran is often mentioned because many scientific computing libraries that NumPy interfaces with are written in Fortran, another language known for numerical efficiency. This further enhances NumPy’s performance.
Priyanka . 10:05 AM  
Not related to pandas or numpy, in real life, does companies use jupyer notebooks or they yse python files ?
Priyanka . 10:05 AM 
use*
IK Academic Support 10:06 AM 
In real life, companies use both Jupyter notebooks and Python files. Jupyter notebooks are popular for exploratory data analysis, visualization, and sharing results, while Python files are commonly used for production code, scripts, and deploying applications due to their robustness and simplicity.
Ravikanth Kompella 10:15 AM  
how about unstructured data, which modules do we use?
IK Academic Support 10:16 AM 
Your doubt is not clear to us. Can you please provide more details about it?
Ravikanth Kompella 10:16 AM 
Pandas is used more for structed data right, I'm looking for unstructured data option as well
Siavash Alemzadeh 10:22 AM 
Depends on the application - e.g., NLP has its own libraries for text processing and CV require other libraries.
Santosh Singh 10:16 AM  
do we use pandas only for eda or do we also use it in production code?
IK Academic Support 10:16 AM 
Pandas is used for both EDA and production code. While it's widely used for data exploration, cleaning, and analysis, it's also used in production environments for data manipulation, preprocessing, and integration tasks in data pipelines and applications.
Santosh Singh 10:17 AM 
thank you!
Santosh Singh 10:18 AM  
is pandas series numpys 1 dimentional ndarray ?
Siavash Alemzadeh 10:21 AM 
You can think of Pandas series as 1-dim numpy array since they have many similarities, but they are of different types in Python due to some minor differences.
Santosh Singh 10:29 AM 
thank you!
Ravikanth Kompella 10:18 AM  
is it AI answering our questions here?
Ravikanth Kompella 10:19 AM 
cuz when I ask calss context based questions I got same answer thrice so far "Your doubt is not clear to us. Can you please provide more details about it?"
Ravikanth Kompella 10:21 AM 
Also after I clarify, there is no response.
Siavash Alemzadeh 10:23 AM 
Just responded to the previous question - Please let me know if any question is unanswered and I do my best to address that. Thank you!
Ravikanth Kompella 10:24 AM 
Thanks Siavash, can you please share if AI is answering our questions here?
IK Academic Support 10:28 AM 
Hi RaviKanth,
It was me answering the question. The question was actually not clear to me so I asked for more details. In zoom when you respond to a already answered question then it doesn't get populated to top. In these cases you can ask the same question again which populates it to top.
Ravikanth Kompella 10:31 AM 
Thanks, no worries!
Ravikanth Kompella 10:29 AM  
Thanks for the clarification, structured answers seemed like AI answers, that's all
IK Academic Support 10:31 AM 
Thanks for the feedback. We try our best to give structured answers so that learner's don't get confused.
Soumodeep Das 10:31 AM  
can python numpy support for than 2d array (3d or 4d), if yes can we have one practical example?
IK Academic Support 10:32 AM 
Yes, it's supported.
Here's an example

import numpy as np
array_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                     [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])

print(array_3d)
This represents 2 matrices each of size 3x4.
Praveen Dhamija 10:34 AM  
How do you filter rows by label? Do rows have labels? Thx
IK Academic Support 10:35 AM 
Yes, rows can have labels in pandas DataFrames. To filter rows by label, you use the .loc[]

Here's an example

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['row1', 'row2', 'row3'])

filtered = df.loc[['row1', 'row3']]
vikash jha 10:38 AM  
dorpna is not available or not a number ?
IK Academic Support 10:40 AM 
it's a method which remove rows with any NaN values.
Praveen Dhamija 10:42 AM  
are pandas dataframe mutable? how does drop and replace work? do we get updated result in same dataframe OR different/new?
Santosh Singh 10:43 AM 
yes
IK Academic Support 10:43 AM 
Yes, pandas DataFrames are mutable.

By default, dropna() returns a new DataFrame with the missing values removed. It does not modify the original DataFrame unless you specify inplace=True.
Priyanka . 10:44 AM  
why I am getting following in jupyter notebook -ModuleNotFoundError: No module named 'pandas'
IK Academic Support 10:45 AM 
Have you install pandas? If not, can you please install it using !pip install pandas
Priyanka . 10:46 AM 
this intruction is missing here
IK Academic Support 10:57 AM 
!pip install pandas
Soumodeep Das 10:46 AM  
how the columns names were created in dataframe?
IK Academic Support 10:47 AM 
These are create while creating the dataframe like this

import pandas as pd
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
})
Priyanka . 10:47 AM  
where can I find this jupyter notebook
IK Academic Support 10:47 AM 
It will be available on UpLevel after the class.
Priyanka . 10:48 AM 
how can we follow along
Debobrata Dutta 10:54 AM 
You can install Anaconda , where you will get everythin's in one shop. https://www.anaconda.com/download
Debobrata Dutta 10:51 AM  
between loc and iloc , which one is more faster?
IK Academic Support 10:53 AM 
iloc is generally faster than loc because iloc uses integer-based indexing, which is simpler and more direct, while loc uses label-based indexing, which involves additional lookups.
Srividya Ananthasubramoney 10:53 AM  
0,2 printed two rows 0 and 2 for data frame  . How to print all 3 rows
IK Academic Support 10:54 AM 
For printing all rows, you can do print(df)

If you want to specifically select all rows using index positions:
print(df.iloc[:])
Praveen Dhamija 10:53 AM  
what is the "type" for condition?
IK Academic Support 10:53 AM 
it's boolean i.e 0 or 1
Naresh Kumar 10:54 AM  
are the braces for the condition(s) mandatory or convention?
IK Academic Support 10:55 AM 
it's better to use them to remove ambiguity while evaluating multiple sub conditions
Priyanka . 10:56 AM  
why I am getting "AttributeError: module 'pandas' has no attribute 'DataFrame'" while doing -df = pd.DataFrame(data)
IK Academic Support 10:58 AM 
Can you please share the complete code which you are trying to run?
Priyanka . 10:58 AM 
data={"Name": ["a", "b", "c"],
      "age": [10,20,30]
      }
Priyanka . 10:58 AM 
df = pd.DataFrame(data)
Priyanka . 11:00 AM  
import numpy as np
import pandas as pd

data={"Name": ["a", "b", "c"],
      "age": [10,20,30]
      }

df = pd.DataFrame(data)
Priyanka . 11:01 AM 
this is python code in .py. Not sure how to share indivual instruction in jupyer notebook
IK Academic Support 11:01 AM 
I just ran this code

import numpy as np
import pandas as pd

data={"Name": ["a", "b", "c"],
      "age": [10,20,30]
      }

df = pd.DataFrame(data)

it is working completely fine. Can you please check if pandas is correctly install in your notebook.
Priyanka . 11:07 AM 
my file name was pandas.py , chatgpt sugeested to rename it to something else
IK Academic Support 11:09 AM 
Yes, it will confuse the Pandas libray with your pandas file. After changing name it will work fine
Frankie Liu (You) 11:04 AM  
how do you refer to the original index after reset_index
IK Academic Support 11:05 AM 
After using reset_index(), the original index is moved to a new column named 'index' by default. You can refer to it like this:

df_reset = df.reset_index()
original_index = df_reset['index']
Frankie Liu (You) 11:06 AM  
how does one reference the row labels
IK Academic Support 11:07 AM 
To reference row labels, use .loc[] with the label. 

row = df.loc['label']
Priyanka . 11:07 AM  
import numpy as np
import pandas as pd

data={"Name": ["a", "b", "c"],
      "age": [10,20,30]
      }

df = pd.DataFrame(data)

print(df)

df.sort_values(by="age", ascending=False)

print(df) -> Why values are not printed in descending order
IK Academic Support 11:10 AM 
The sort_values() method returns a new DataFrame sorted by the specified column but does not modify the original DataFrame in place by default. To see the sorted DataFrame, either assign it back to df or use the inplace=True parameter.
Frankie Liu (You) 11:08 AM  
I want all the row labels and put it in an array
IK Academic Support 11:08 AM 
To get all row labels as an array, You can use

row_labels = df.index.to_numpy()
Lakshmi Akkiraju 11:10 AM  
The notebook is shared in https://drive.google.com/drive/folders/1xp-RO0HausrHirHnL_3Eo6gmDMoHp4pU
This question has been answered live
Lijing Bu 11:11 AM  
For Numpy https://drive.google.com/drive/folders/1ledXv9FWP_zGfMHpvoILj-noWcTCmNTE?usp=drive_link
This question has been answered live
Lijing Bu 11:13 AM  
The ipynb is under the pre-class note or below the video of class schedule. Opened after Thursday class. It’s a not so obvious link under the video or the class schedule.
IK Academic Support 11:15 AM 
Please post all non-academic queries in the Chat section. Alternatively, you can also sent us an email on operations@interviewkickstart.com
Priyanka . 11:31 AM 
Lijing , where is pre-class note ?
Frankie Liu (You) 11:14 AM  
NaN != None Correct?  Thought I heard they were the same.
IK Academic Support 11:15 AM 
Yes, NaN (Not a Number) and None are not the same, though they are often used to represent missing or undefined values.
Frankie Liu (You) 11:15 AM  
Is a string NaN?
IK Academic Support 11:16 AM 
No, a string is not considered NaN. NaN (Not a Number) is a special floating-point value used to represent missing or undefined numerical data
Lakshmi Govindasamy 11:20 AM  
after reset index..  both original index and new index present in the df. In this case iloc will work on new idx or old idx
IK Academic Support 11:20 AM 
iloc will work with the new integer-based index, not the original index.
Frankie Liu (You) 11:23 AM  
how does concat react to different column names (and row names)
IK Academic Support 11:24 AM 
When using concat with different column names, it aligns data by column names and fills missing values with NaN where columns don't match. For different row names, it aligns data by row labels and adds rows with labels not present in all DataFrames.
Frankie Liu (You) 11:26 AM  
For columns, then it does an "outer join" ?
IK Academic Support 11:27 AM 
Yes, when concatenating DataFrames along rows (with axis=0), pandas performs an "outer join" by default. This means it aligns DataFrames based on their row labels and fills missing values with NaN where row labels do not match.
Frankie Liu (You) 11:27 AM  
Oops  meant rows.
This question has been answered live
Frankie Liu (You) 11:30 AM  
why does aggregate in .agg take a string and not a function reference?
IK Academic Support 11:30 AM 
.agg() accepts both strings (for predefined functions) and function references to provide flexibility and ease of use. Strings simplify common operations, while function references allow for custom aggregations.
Srividya Ananthasubramoney 11:30 AM  
Can you explain reetindex means?
Srividya Ananthasubramoney 11:30 AM 
I mean resetindex
IK Academic Support 11:31 AM 
reset_index() resets the index of a DataFrame to the default integer index, and optionally moves the current index to a column. This is useful for reordering rows or when the index is no longer needed.
Tsegaye Abebe 11:34 AM  
Is this gives you error if the axis is 1?
IK Academic Support 11:39 AM 
Can you please let me which code snippet you are referring to here?
Tsegaye Abebe 11:51 AM 
Thank you I got it from his lecture
Nishant Upadhyay 11:34 AM  
Lets detail axis please
IK Academic Support 11:36 AM 
axis specifies the direction of operation:

axis=0: Refers to rows (vertical axis). Operations are applied across columns.
axis=1: Refers to columns (horizontal axis). Operations are applied across rows.
For example, df.sum(axis=0) sums values column-wise, while df.sum(axis=1) sums values row-wise.
Praveen Dhamija 11:34 AM  
how to access the original index values when we do reset_index = True?
IK Academic Support 11:36 AM 
When using reset_index(inplace=True), the original index values are moved to a new column named 'index' by default. You can access these values with:
original_index = df['index']
Nishant Upadhyay 11:36 AM  
Does the axis has only 2 values , 0 for
 extend rows  and 1 for extending columns ?
IK Academic Support 11:36 AM 
yes
Lakshmi Govindasamy 11:37 AM  
how do you add a new column to the df or add a computed column?
IK Academic Support 11:38 AM 
To add new column:
df['new_column'] = [value1, value2, value3]

To add computed column:
df['computed_column'] = df['existing_column'] * 2
Giridhar Narayanan 11:37 AM  
Can you explain rationale behind calling horizontal concatenation as axis=1 and axis=0 for vertical concat
IK Academic Support 11:38 AM 
axis=0: Refers to vertical concatenation (stacking rows), as it adds data along the row axis.
axis=1: Refers to horizontal concatenation (adding columns), as it adds data along the column axis.
Praveen Dhamija 11:41 AM  
can we join on multiple columns?
IK Academic Support 11:41 AM 
Yes, you can join on multiple columns by passing a list of column names to the on parameter in method like .merge().

df1.merge(df2, on=['col1', 'col2'])
Senthilkumar Rajamanickam 11:41 AM  
Can we merge only 2 cant we do more?
IK Academic Support 11:42 AM 
Yes, you can merge more than two DataFrames. You simply chain .merge() calls or pass a list of DataFrames to a merging function if needed.

df1.merge(df2, on='key').merge(df3, on='key')
Debobrata Dutta 11:42 AM  
Anything's for cross join?
IK Academic Support 11:42 AM 
To perform a cross join, use merge() with how='cross' or manually create a Cartesian product using pd.merge() without specifying keys.


df1.merge(df2, how='cross')
Lalit Mande 11:42 AM  
how we can assign default value if condition is not matched ?
IK Academic Support 11:43 AM 
You can use np.where()  to assign default values when a condition is not met.

import numpy as np

df['new_column'] = np.where(df['condition_column'] > 0, df['value_if_true'], 'default_value')
Lalit Mande 11:44 AM 
thank you
Senthilkumar Rajamanickam 11:42 AM  
Whats the difference between inner and outer merge?
IK Academic Support 11:44 AM 
Inner merge  Includes only rows with matching keys in both DataFrames. Non-matching rows are excluded. While outer merge Includes all rows from both DataFrames. Non-matching rows are filled with NaN.
Lakshmi Akkiraju 11:45 AM 
Outer can be treated as union. is that right?
IK Academic Support 11:49 AM 
Yes, that's correct. An outer merge can be thought of as a union of the two DataFrames, including all rows from both and filling missing values with NaN.
Frankie Liu (You) 11:46 AM  
in sql you can join based on a condition, how can you do it with merge?
IK Academic Support 11:49 AM 
you can join based on a condition using merge() with the on parameter for exact matches or by using query() to filter the results after merging.

# Exact match join
df1.merge(df2, on='key')

# Conditional join (e.g., merge on a range)
df1.merge(df2, how='inner', left_on='key1', right_on='key2').query('key1 > key2')
Debobrata Dutta 11:54 AM  
I think if we go with diamention then it will always be row * column , so row is axis 0 and column is axis 1, that's why in python when we are concatenating with axis 0 it's concatenating row wise , for axis 1 it's concatanating column wise
This question has been answered live
Sunil Sharma 12:04 PM 
Thats correct
IK Academic Support 12:07 PM 
No, right now Zoom doesn't support this feature
