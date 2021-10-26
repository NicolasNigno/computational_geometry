import cv2, numpy as np, sys

if len( sys.argv ) < 3:
  print( 'Usage: python ' + sys.argv[ 0 ] + ' input output' )
  sys.exit( 1 )
# end if
input_filename = sys.argv[ 1 ]
output_filename = sys.argv[ 2 ]

input_image = cv2.imread(input_filename)
output_str = ''

matrix = input_image[:,:,0]
w = 3

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        value = matrix[i,j]
        m = np.array([value])
         
        for r in range(0,w):
            for c in range(0,w):
                 
                try:
                    aux = np.array([matrix[(i-round(w/2))+r,(j-round(w/2))+c]])
                except IndexError:
                    aux = np.array([np.nan])
                 
                m = np.append(m, aux, axis=0)
                 
        if (i==0 and j==0) or (i==(matrix.shape[0]-1) and j==0) or (i==0 and j==(matrix.shape[1]-1)) or (i==(matrix.shape[0]-1) and j==(matrix.shape[1]-1)) or value != np.median(m):
            output_str += str( i ) + ' ' + str( j ) + ' '
            output_str += str( value / 10.0 ) + '\n'

output_file = open( output_filename, 'w' )
output_file.write( output_str )
output_file.close( )


## eof - $RCSfile$