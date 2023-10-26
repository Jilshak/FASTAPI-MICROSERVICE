import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

function HomePage() {

  const navigate = useNavigate()

  const [movies, setMovies] = useState([])

  // add moveis
  const [toggle, setToggle] = useState(false)

  const [title, setTitle] = useState('')
  const [plot, setPlot] = useState('')
  const [genres, setGenres] = useState('')
  const [casts, setCasts] = useState('')

  useEffect(() => {
    handleGetMovies()
  }, [])

  const handleLogOut = async () => {
    localStorage.removeItem('fastauth')
    await navigate('/login')
  }

  const handleGetMovies = async () => {
    const request = await axios.get('http://127.0.0.1:8001/')
    const response = await request.data
    console.log(response)
    if (request.status == 200) {
      await setMovies(response)
      return
    }
  }

  const cleanUp = () => {
    setCasts('')
    setTitle('')
    setGenres('')
    setPlot('')
  }

  const handleAddMovies = async () => {

    const credentials = {
      title: title,
      plot: plot,
      casts: casts,
      genres: genres
    }

    const request = await axios.post('http://127.0.0.1:8001/', credentials, {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      }
    })
    const response = await request.data
    if (request.status == 200) {
      await window.location.reload()
    } else {
      alert("Something went wrong while addin the movie")
    }
    await cleanUp()
    setToggle(false)
    
  }

  return (
    <div>
      {
        toggle ?
          <>
            <div className='flex items-center justify-center '>
              <div className='h-[500px] w-[400px] rounded-lg shadow-2xl absolute bottom-52 '>
                <div className='flex justify-center my-5 font-bold text-2xl'>
                  <h2>Add Movie</h2>
                </div>
                <div className='flex justify-center my-4'>
                  <input onChange={(e) => setTitle(e.target.value)} value={title} className=' bg-[#e1dfdf] outline-2 h-[30px] w-3/4 pl-2 text-black' type="text" placeholder='title' />
                </div>
                <div className='flex justify-center my-4'>
                  <input onChange={(e) => setGenres(e.target.value)} value={genres} className=' bg-[#e1dfdf] outline-2 h-[30px] w-3/4 pl-2 text-black' type="text" placeholder='genres' />
                </div>
                <div className='flex justify-center my-4'>
                  <input onChange={(e) => setPlot(e.target.value)} value={plot} className=' bg-[#e1dfdf] outline-2 h-[30px] w-3/4 pl-2 text-black' type="text" placeholder='plot' />
                </div>
                <div className='flex justify-center my-4'>
                  <input onChange={(e) => setCasts(e.target.value)} value={casts} className=' bg-[#e1dfdf] outline-2 h-[30px] w-3/4 pl-2 text-black' type="text" placeholder='casts' />
                </div>
                <div className='my-5 flex items-center justify-center'>
                  <button onClick={handleAddMovies} className='w-[150px] h-[40px] bg-[#e4e3e3] rounded-lg hover:bg-green-300 hover:text-white'>ADD MOVIE</button>
                </div>
                <div className='my-5 flex items-center justify-center'>
                  <button onClick={(e) => setToggle(false)} className='w-[150px] h-[40px] bg-[#e4e3e3] rounded-lg hover:bg-red-300 hover:text-white'>Cancel</button>
                </div>
              </div>

            </div>
          </> : null
      }
      <div className='flex items-center justify-end'>
        <button onClick={handleLogOut} className='bg-red-400 h-10 w-[100px] rounded-lg text-white text-lg my-5 mx-5'>Logout</button>
      </div>
      <div>
        <div className='flex justify-around'>
          <div className='flex items-start w-full'>
            <h1 className='font-bold text-3xl mx-5'>Movies</h1>
          </div>
          <button onClick={(e) => setToggle(true)} className='bg-red-300 w-[50px] mx-7 text-white font-bold rounded-md hover:bg-red-600'>Add</button>
        </div>
        {
          movies?.length >= 1 ?
            <div>
              {
                movies?.map((item) => {
                  return (
                    <div className='bg-[#e2e1e1] h-10 w-60 my-5 mx-5 text-center flex items-center justify-center shadow-lg hover:shadow-xl'>
                      <p className='turncate w-full'>{item.title}</p>
                    </div>
                  )
                })
              }
            </div> : <p>loading....!!!</p>
        }
      </div>
    </div>
  )
}

export default HomePage
