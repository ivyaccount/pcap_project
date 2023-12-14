WSPACE = 	..

CXXFLAGS =	-O3 -g -Wall -fmessage-length=0 -I$(WSPACE)/cdcl -D __STDC_LIMIT_MACROS -D __STDC_FORMAT_MACROS

OBJS =		hordesat.o utilities/ClauseFilter.o solvers/CDCL.o utilities/ClauseDatabase.o \
			utilities/SatUtils.o utilities/Logger.o sharing/AllToAllSharingManager.o \
			sharing/LogSharingManager.o

LIBS =		-lz -L$(WSPACE)/CDCL/ -llgl

TARGET =	hordesat

CXX = 		mpic++

$(TARGET):	$(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LIBS)

all:	$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)
