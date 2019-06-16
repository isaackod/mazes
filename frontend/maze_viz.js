
			//Width and height
			var width = 400;
			var height = 400;

            // Data loading is asynch, so all code is in this block
            d3.json("default_maze.json").then(function(cells){

                    
                var xScale = d3.scaleBand()
                                .domain(d3.range(cells.Dims[0]))
                                .rangeRound([0,width])
                                .paddingInner(0.00);

                var yScale = d3.scaleBand()
                                .domain(d3.range(cells.Dims[1]))
                                .rangeRound([0,height])
                                .paddingInner(0.00);

                var svg = d3.select("body")
                                .append("svg")
                                .attr("width",width)
                                .attr("height",height)

                svg.selectAll("rect")
                    .data(cells.cells)
                    .enter()
                    .append("rect")
                    .attr("x", function(d){
                        return xScale(d.loc[0]);
                    })
                    .attr("y", function(d){
                        return yScale(d.loc[1]);
                    })
                    .attr("width", xScale.bandwidth())
                    .attr("height", yScale.bandwidth())
                    .transition()
                    .delay(function(d) {
                        return d.weight*5;
                    }
                    )
                    .duration(2000)
                    .ease(d3.easeElasticOut)
                    .attr("fill", function(d) {
                        return "rgb(0, 0, " + Math.min(255,d.weight) + ")";
                    });

                lines = svg.selectAll("line")
                    .data(cells.cells)
                    .enter();
                // .append("g");
                
                var x = xScale.bandwidth();
                var y = yScale.bandwidth();
                    
                //top        
                lines.append("line")
                    .attr("x1", function(d){
                        return xScale(d.loc[0]);
                    })
                    .attr("y1", function(d){
                        return yScale(d.loc[1]);
                    })
                    .attr("x2", function(d){
                        return xScale(d.loc[0])+x;
                    })
                    .attr("y2", function(d){
                        return yScale(d.loc[1])
                    })
                    .style("opacity", function(d){
                        if (d.open.includes("N")){
                            return 0;
                        }
                        else{
                            return 1.0;
                        }
                    });
                
                //right
                lines.append("line")
                    .attr("x1", function(d){
                        return xScale(d.loc[0])+x;
                    })
                    .attr("y1", function(d){
                        return yScale(d.loc[1]);
                    })
                    .attr("x2", function(d){
                        return xScale(d.loc[0])+x;
                    })
                    .attr("y2", function(d){
                        return yScale(d.loc[1])+y;
                    })
                    .style("opacity", function(d){
                        if (d.open.includes("E")){
                            return 0;
                        }
                        else{
                            return 1.0;
                        }
                    });


                //bottom         
                lines.append("line")
                    .attr("x1", function(d){
                        return xScale(d.loc[0]);
                    })
                    .attr("y1", function(d){
                        return yScale(d.loc[1])+y;
                    })
                    .attr("x2", function(d){
                        return xScale(d.loc[0])+x;
                    })
                    .attr("y2", function(d){
                        return yScale(d.loc[1])+y;
                    })
                    .style("opacity", function(d){
                        if (d.open.includes("S")){
                            return 0;
                        }
                        else{
                            return 1.0;
                        }
                    });

                //left
                lines.append("line")
                    .attr("x1", function(d){
                        return xScale(d.loc[0]);
                    })
                    .attr("y1", function(d){
                        return yScale(d.loc[1]);
                    })
                    .attr("x2", function(d){
                        return xScale(d.loc[0]);
                    })
                    .attr("y2", function(d){
                        return yScale(d.loc[1])+y;
                    })
                    .style("opacity", function(d){
                        if (d.open.includes("W")){
                            return 0;
                        }
                        else{
                            return 1.0;
                        }
                    });

    

                d3.selectAll("line")
                    .attr("stroke-width", 3)
                    .attr("stroke", 'red');


			});