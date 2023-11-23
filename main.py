from fpdf import FPDF
import pandas as pd # for implementing topics data into pdf

pdf = FPDF(orientation='P', unit='mm', format='A4') # create pdf
pdf.set_auto_page_break(auto=False,margin=0) #every page not to break in pdf if should be attached

df = pd.read_csv('topics.csv')

# pdf.add_page() #it will add pages
#
# pdf.set_font(family='Times',style='B',size = 12) #Times is font , 'B'= Bold, size to size of text
# # Before creating cell we need to create font
#
# pdf.cell(w=0,h=12,txt='Hello There!',align='L',ln=1,border=1) # we will add text to pdf
# pdf.set_font(family='Times',style='B',size = 12)
# pdf.cell(w=0,h=12,txt='Hi There!',align='L',ln=1,border=1)
#w=width , h = height of  the cell , border = create border for each cell
#ln = breakline it will indicate to add in next line Always ln = 1


#pdf.output('output.pdf') #To store the output pdf file we created it.

# it only has one page if need need more page use below comment and start to code like above

#pdf.add_page() from line 5 copied

# The above code modify into using logics to implement topics to pdf

for index,row in df.iterrows():
    pdf.add_page()  # it will add pages

    pdf.set_font(family='Times', style='B', size=12)  # Times is font , 'B'= Bold, size to size of text
    # Before creating cell we need to create font
    pdf.set_text_color(100,100,100) # this combination is gray
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=1)  # we will add text to pdf
    pdf.line(x1= 10,y1 = 21, x2 =200,y2 = 21) # x are range from staring space eg:marigin  # y are ending ponints
    # x and y are size of the lines we have to mark in millimeters
    # becasue in the upper mm we do specify unit =  mm

    #set footer
    pdf.ln(256) #where to place footer for every topics bottom under right corner it will show the topic name
    pdf.set_font(family='Times', style='I', size=0)  # Times is font , 'B'= Bold, size to size of text
    # Before creating cell we need to create font
    pdf.set_text_color(100, 100, 100)  # this combination is gray
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # as of now there is only one page for each topics we need to create pages account the csv file given pages for each topics
    # eg: topic 1(2pages), top 2 (3 pages) given in csv file
    for i in range(row['Pages']-1): # -1 is for index startes from 0 and in csv file it takes heading as 0
        pdf.add_page()
        #to set footer
        pdf.set_font(family='Times', style='B', size=12)  # Times is font , 'B'= Bold, size to size of text
        # Before creating cell we need to create font
        pdf.set_text_color(100, 100, 100)  # this combination is gray
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=1)  # we will add text to pdf
        pdf.line(x1=10, y1=21, x2=200, y2=21)

pdf.output('output.pdf')