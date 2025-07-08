#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('display', 'latex')


# In[2]:


#Defines a 4-dimensional Lorentzian manifold M
M = Manifold(4, name='M',structure='Lorentzian')


# In[3]:


#coordinates on M: u r theta1, theta2
X.<u,r,theta1, theta2>=M.chart('u r theta1:(0,pi) theta2:(0,2*phi)')


# In[4]:


#returns the list of coordinates
X[:]


# In[5]:


#metric functions
U = function('U')(u, r, theta1, theta2)
beta_metric = function('beta_metric')(u, r, theta1, theta2)


# In[6]:


#angular part of the metric 
gamma22 = function('gamma22')(u, r, theta1, theta2)  
gamma23 = function('gamma23')(u, r, theta1, theta2)  
gamma33 = function('gamma33')(u, r, theta1, theta2)  

# symmetry 
gamma32 = gamma23


# In[7]:


#Angular vector components U^A
#UA is vector field on the sphere, so it has two components, UA2=Utheta, UA3=Uphi

VA2 = function('VA2')(u, r, theta1, theta2)  # corresponds to A = 2 (theta1)
VA3 = function('VA3')(u, r, theta1, theta2)  # corresponds to A = 3 (phi

VA = [VA2, VA3]


# In[8]:


#Initializes the metric tensor g on manifold 𝑀
g = M.metric()


# In[9]:


#g_uu

g[0,0] = -U * exp(2 * beta_metric) + r^2 * (gamma22 * VA2^2 + 2 * gamma23 * VA2 * VA3 + gamma33 * VA3^2)


# In[10]:


# g_ur and g_ru
g[0,1] = g[1,0] = -exp(2*beta_metric)


# In[11]:


# g_uthetA and g_thetAu
g[0,2] = g[2,0] = -r^2 * (gamma22 * VA2 + gamma23 * VA3)   # gUTHET
g[0,3] = g[3,0] = -r^2 * (gamma23 * VA2 + gamma33 * VA3)   # gUPHI


# In[12]:


#g_thetA,thetB

g[2,2] = r^2 * gamma22 
g[2,3] = g[3,2] = r^2 * gamma23  
g[3,3] = r^2 * gamma33  


# In[13]:


g.display()


# In[14]:


g[:]


# In[15]:


g.christoffel_symbols_display()


# In[16]:


# Compute the Levi-Civita connection
nabla = g.connection()


# In[17]:


# Compute the Riemann curvature tensor
Riem = nabla.riemann()
Riem.display()


# In[ ]:




