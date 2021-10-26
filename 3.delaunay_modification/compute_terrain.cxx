// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Projection_traits_xy_3.h>
#include <CGAL/Delaunay_triangulation_2.h>
#include <CGAL/draw_triangulation_2.h>
#include <fstream>

using TKernel = CGAL::Exact_predicates_inexact_constructions_kernel;
using TTraits = CGAL::Projection_traits_xy_3< TKernel >;
using TTriangulation = CGAL::Delaunay_triangulation_2< TTraits >;
using TPoint = TKernel::Point_3;

int main( int argc, char** argv )
{
  std::ifstream in( argv[ 1 ] );
  auto b = std::istream_iterator< TPoint >( in );
  auto e = std::istream_iterator< TPoint >( );
  TTriangulation triangulation( b, e );
  in.close( );

  CGAL::draw( triangulation );

  return( EXIT_SUCCESS );
}

// eof - $RCSfile$
