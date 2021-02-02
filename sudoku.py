# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd

def check_row(n,i,X):
    if n in X[i]:
        #print ('{} is not a valid entry'.format(n))
        return False
    else:
        return True
    
def check_column(n,j,X):
    if n in X[:,j]:
        #print ('{} is not a valid entry'.format(n))
        return False
    else:
        return True
    
def BOX(X):
    return np.array([[X[3*i:3*(i+1), 3*j:3*(j+1)] for j in range(3)] for i in range(3)])
    
def check_box(n,i,j,X):
    if n in BOX(X)[int(i/3)][int(j/3)]:
        #print ('{} is not a valid entry'.format(n))
        return False
    else:
        return True
    
def check_position(n,i,j,X):
    if n in range(1,10):
        return check_row(n,i,X) and check_column(n,j,X) and check_box(n,i,j,X)
    else:
        return False

def update(n,i,j,Y):
    X=Y.copy()
    if np.isnan(X[i][j])==False:
        #print('entry not successful')
        return X
    elif n not in list(range(1,10)):
        #print ('{} is not a valid entry'.format(n))
        return X
    elif check_position(n,i,j,X):
        X[i][j]=n
        return X
    else:
        return X
    
    
def possible_entries(i,j,X):
    e=[]
    if np.isnan(X)[i,j]== False:
        return []
    else:
        for n in range(1,10):
            if check_position(n,i,j,X):
                e.append(n)
        return e

def initial_entries(Y):
    X=Y.copy()
    p_e=[[possible_entries(i,j,X) for j in range(9)] for i in range(9)]
    a=81
    m=0
    while np.isnan(X).sum() != a:
        a=np.isnan(X).sum()
        for i in range(9):
            for j in range(9):
                if len(p_e[i][j])==1:
                    X=update(p_e[i][j][0],i,j,X)
                    #print('{} put in row: {}, column: {}'.format(p_e[i][j][0],i,j))
        m+=1
       #print('{} iteration done'.format(m))
        p_e= [[possible_entries(i,j,X) for j in range(9)] for i in range(9)]
    return X

def index_of_column(n,j,X):
    """
    gives a list of indexes on column j where number n can sit
    """
    a=[]
    for i in range(9):
        if np.isnan(X)[i,j]:
            if n not in X[i]:
                if n not in BOX(X)[int(i/3)][int(j/3)].flatten():
                    a.append(i)
    return a

def index_of_row(n,i,X):
    """
    gives list of indexes on row i where number n can sit
    """
    a=[]
    for j in range(9):
        if np.isnan(X)[i,j]:
            if n not in X[:,j]:
                if n not in BOX(X)[int(i/3)][int(j/3)]:
                    a.append(j)
    return a        

def index_of_box(n,i,j,X):
    """
    gives list of indexes on ith row, jth column box where number n can sit
    """
    a=[]
    box_row= int(i/3)
    box_column= int(j/3)
    box=BOX(X)[box_row][box_column].flatten()
    for k in range(len(box)):
        if np.isnan(X)[i,j]:
            if n not in X[i]:
                if n not in X[:,j]:
                    a.append([3*box_row+int(k/3),3*box_column+k%3])
    return a 

def half_solution(Y):
    X=Y.copy()
    a=81
    m=0
    while a != np.isnan(X).sum():
        a=np.isnan(X).sum()
        for n in range(1,10):
            for j in range(9):
                if len(index_of_column(n,j,X))==1:
                    X=update(n, index_of_column(n,j,X)[0], j, X)
        for n in range(1,10):
            for i in range(9):
                if len(index_of_row(n,i,X))==1:
                    X=update(n, i, index_of_row(n,i,X)[0], X)
                    
        for n in range(1,10):
            for i in range(9):
                for j in range(9):
                    if len(index_of_box(n,i,j,X))==1:
                        l=index_of_box(n,i,j,X)[0]
                        X= update(n,l[0],l[1] ,X)
        #print('iteration {} done. Remaining missing values: {} '.format(m+1, np.isnan(X).sum()))
        m+=1
    return X
 
def rec_sol(Y):
    a=81
    n1=0
    X=Y.copy()
    while a != np.isnan(X).sum():
        a=np.isnan(X).sum()
        X=initial_entries(X)
        X=half_solution(X)
        n1 +=1
        #print('after {} sets of recurrsion missing value left: {}'.format(n1,np.isnan(X).sum()))
        
    return X  

def trial_or_error(Y, record=[]):
    X= Y.copy()
    #print('copy done')
    a= (np.array([[len(possible_entries(i,j,X)) for j in range(9)] for i in range(9)])==0).sum()
    b= np.isnan(X).sum()
    X=rec_sol(X)
    while (a != 81) :
        #print('enter while loop')
        lentry=np.array([[len(possible_entries(i,j,X)) for j in range(9)] for i in range(9)])
        lentry[lentry==0]=11
        #print(lentry)
        k=lentry.flatten().argmin()
        #print('k={}'.format(k))
        p_e=possible_entries(int(k/9),k%9,X)
        Z=list(X.copy())
        X=update(p_e[0],int(k/9),k%9,X)
        #print('update{},{},{}'.format(p_e[0],int(k/9),k%9))
        X=rec_sol(X)
        record.append([p_e[0],int(k/9),k%9,p_e,Z])
        a= (np.array([[len(possible_entries(i,j,X)) for j in range(9)] for i in range(9)])==0).sum()
        b= np.isnan(X).sum()
        
    if (b !=0):
        return record
    
    elif b==0:
        #print('Final Solution is: ')
        return X

def reconsile (m):
    r=m.copy()
    k=r[-1]
    r=r[:-1]
    puzzle_before_last_error=np.array(k[-1])
    wrong_entry= k[0]
    entry_row=k[1]
    entry_column= k[2]
    possible_entries_on_last_error= k[3]
    p_e=[i for i in possible_entries_on_last_error if i != wrong_entry]
    #print(p_e,k,r)
    record=r.copy()
    i=1
    #print(i)
    
    if len(p_e)==1:
        #print('entered if')
        Z=list(puzzle_before_last_error.copy())
        fam=update(p_e[0], entry_row, entry_column,puzzle_before_last_error)
        #print(puzzle_before_last_error)
        fill_and_more=rec_sol(fam)
        record.append([p_e[0], entry_row, entry_column,p_e,Z])
        b=np.isnan(fill_and_more).sum()
        a= (np.array([[len(possible_entries(i,j,fill_and_more)) for j in range(9)] for i in range(9)])==0).sum()
        if b==0:
            #print('solution found')
            return fill_and_more
        elif a==81:
            i+=1
            #print ('going back one step')
            return reconsile(r)
        else:
            #print ('Another branch')
            return trial_or_error(fill_and_more, record)
    else:
        #print('entered else')
        Z=list(puzzle_before_last_error.copy())
        fam=update(p_e[0], entry_row, entry_column,puzzle_before_last_error)
        fill_and_more=rec_sol(fam)
        b=np.isnan(fill_and_more).sum()
        a= (np.array([[len(possible_entries(i,j,fill_and_more)) for j in range(9)] for i in range(9)])==0).sum()
        record.append([p_e[0], entry_row, entry_column,p_e,Z])
        if b==0:
            #print('solution found')
            return fill_and_more
        elif a==81:
            i+=1
            #print('going back a step')
            return reconsile(r)
        else:
            #print('Another branch')
            return trial_or_error(fill_and_more,record)

def solver (y):
    X=y.copy()
    X=rec_sol(X)
    c=trial_or_error(X)
    while np.array(c).shape != (9,9):
        c=reconsile(c)
    return c
    

def inp():
    superlist=[]
    for i in range(9):
        l=[]
        for j in range(9):
            entry= int(input('Enter {} row {} column. Put 0 for blank.'.format(i+1,j+1)))
            if entry==0:
                entry= np.nan
            l.append(entry)
        superlist.append(l)
    superlist= np.array(superlist)
    return superlist

if __name__=='__main__':
    pass


"""
extreme=inp()
    
k=solver(extreme)
print(k)
"""