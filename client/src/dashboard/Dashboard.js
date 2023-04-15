import React, { useState } from 'react'
import Chart from './Chart';
import Deposits from './Deposits';
import Orders from './Orders';
import { Box,Toolbar,Container,Grid,Paper, Stack,Chip } from '@mui/material';
import { columns } from './Data';
import Title from './Title';

function createData(id, date, name, shipTo, paymentMethod, amount) {
  return { id, date, name, shipTo, paymentMethod, amount };
}

const rows = [
  createData(
    0,
    '16 Mar, 2019',
    'Elvis Presley',
    'Tupelo, MS',
    'VISA ⠀•••• 3719',
    312.44,
  ),
  createData(
    1,
    '16 Mar, 2019',
    'Paul McCartney',
    'London, UK',
    'VISA ⠀•••• 2574',
    866.99,
  ),
  createData(2, '16 Mar, 2019', 'Tom Scholz', 'Boston, MA', 'MC ⠀•••• 1253', 100.81),
  createData(
    3,
    '16 Mar, 2019',
    'Michael Jackson',
    'Gary, IN',
    'AMEX ⠀•••• 2000',
    654.39,
  ),
  createData(
    4,
    '15 Mar, 2019',
    'Bruce Springsteen',
    'Long Branch, NJ',
    'VISA ⠀•••• 5919',
    212.79,
  ),
];

const Dashboard = () => {
  const [cols,setCols] = useState([]);
  return (
    <Box
    component="main"
    sx={{
      backgroundColor: (theme) =>
        theme.palette.mode === 'light'
          ? theme.palette.grey[100]
          : theme.palette.grey[900],
      flexGrow: 1,
      height: '100vh',
      overflow: 'auto',
    }}
  >
    <Toolbar />
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Grid container spacing={3}>
        {/* Chart */}
        <Grid item xs={12} md={8} lg={9}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
              height: 240,
            }}
          >
            <Chart />
          </Paper>
        </Grid>
        {/* Recent Deposits */}
        <Grid item xs={12} md={4} lg={3}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
              height: 240,
            }}
          >
            <Deposits />
          </Paper>
        </Grid>
        {/* Recent Orders */}
        <Grid item xs={12}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <Title>Available Columns</Title>
            <Stack direction={'row'} spacing={2} flexWrap={'wrap'}>
            {columns.filter(c => !cols.includes(c)).map(col=>
                <Chip
                label={col}
                key={col}
                // onClick={(e)=>setCols(cols => [...cols,e.target.value])}
                onClick={()=>setCols(cols => [...cols,col])}
                />
                )}
            </Stack>
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <Title>Selected Columns</Title>
            <Stack direction={'row'} spacing={2} flexWrap={'wrap'}>
              {cols.map(col=>
                <Chip
                label={col}
                key={col}
                onClick={()=>setCols(cols => cols.filter(c => c !== col))}
                onDelete={()=>setCols(cols => cols.filter(c => c !== col))}
                />
                )}
            </Stack>
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>

            <Orders rows={rows}/>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  </Box>
  )
}

export default Dashboard