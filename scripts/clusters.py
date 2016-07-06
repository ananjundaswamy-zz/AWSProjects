import boto3
import os
import pwd

def list_clusters():
   print "Listing clusters belonging to user %s" %(pwd.getpwuid( os.getuid() ).pw_name)

def create_cluster():
   print "Creating ECS cluster"

def delete_cluster(clusterName):
   print "Deleting cluster %s" %clusterName

