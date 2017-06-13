#!/usr/bin/python


import glob

# import the packages for logging 
import logging
import logging.handlers
import logging.config

module_logger = logging.getLogger("tracker.Parameters")

# class for the parameter object
class Parameters( object ):

    # initialization of tracker
    def __init__( self ):
        """Summary line.
    
       Extended description of function.
    
       Args:
           arg1 (int): Description of arg1
           arg2 (str): Description of arg2
    
       Returns:
           bool: Description of return value
    
        """
            
        logger = logging.getLogger("tracker.Parameters._init_" )
        logger.info('Reading the parameters' )        
        
        # dataset information
        dataset_path = '/home/mathew/Documents/DATASET/'

        dataset_name = 'vot2014'

        sequence_name= 'ball'

        image_extension = '.jpg'
        
        ground_truth_file = 'groundtruth.txt'
        
        self._dict_type = 2
        
        self._dict_size  = 25
        self._nonzero_coefs = 5
        
        sequence_path = dataset_path + dataset_name + '/' + sequence_name + '/'
        
        ground_truth_file_path = sequence_path +'/' + ground_truth_file
        
        ground_truth_file_content = open( ground_truth_file_path )
        
              
        lines = ground_truth_file_content.readlines()
        
        self._seq_name = sequence_name
        
        self._isColor = True
        
        # 2D list of ground truth values
        self._ground_truth = [ map( float,line.strip().split(',')) for line in lines] 
        
        self._ground_truth = [ map( int , i ) for i in  self._ground_truth ]
        
        
        # list containing the names of the frames in the sequence
        self._image_name_list = glob.glob( sequence_path + '*' + image_extension )
        
        # sort the list in the ascending order
        self._image_name_list.sort() 
        
        self._start_frame_no = 0
        
        self._end_frame_no = len( self._image_name_list ) -1
        
        # minimum size of the patch 
        self._min_patch_size = 7

        self._min_cell_size = 15
        
        self._patch_size = 7
        
        self._stride_x = 1 
        
        self._stride_y = 1
        
             
        self._cell_height  = 10
        
        self._cell_width  = 10
        
        
        
        
        
        
            
            
       
        
        
        
        
        
        
        